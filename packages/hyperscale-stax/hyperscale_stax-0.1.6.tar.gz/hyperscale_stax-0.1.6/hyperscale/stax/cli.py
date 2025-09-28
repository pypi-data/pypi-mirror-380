import tempfile
import time
import zipfile
from pathlib import Path

import boto3
import cfnlint
import click
from botocore.exceptions import ClientError
from sigstore.errors import VerificationError

from hyperscale.stax.manifest import DeployMethod
from hyperscale.stax.manifest import load_manifest_from_path
from hyperscale.stax.sigstore import verify_bundle_signature


@click.group()
@click.version_option(package_name="hyperscale.stax")
def main():
    """Deploy CloudFormation Stack Sets"""
    pass


@main.command()
@click.option(
    "-p", "--prefix", default="stax", help="A prefix to add to all stack names"
)
@click.option(
    "-s",
    "--sigstore-bundle",
    default=None,
    required=False,
    type=click.Path(exists=True),
    help="Path to a Sigstore bundle to verify",
)
@click.option(
    "-i", "--oidc-identity", default=None, help="OIDC identity to verify against"
)
@click.option("-r", "--oidc-issuer", default=None, help="OIDC issuer to verify against")
@click.argument("archive", required=True, type=click.Path(exists=True))
def deploy(archive, prefix, sigstore_bundle, oidc_identity, oidc_issuer):
    """Deploy the archive"""
    archive_path = Path(archive)

    if archive_path.suffix.lower() != ".zip":
        raise click.BadParameter("archive must be a .zip file", param_hint=["archive"])

    if not zipfile.is_zipfile(archive_path):
        raise click.BadParameter(
            "archive is not a valid ZIP archive", param_hint=["archive"]
        )

    if any([sigstore_bundle, oidc_identity, oidc_issuer]) and not all(
        [sigstore_bundle, oidc_identity, oidc_issuer]
    ):
        raise click.BadParameter(
            "must provide all of sigstore-bundle, oidc-identity, oidc-issuer or none "
            "of them",
            param_hint=["sigstore-bundle", "oidc-identity", "oidc-issuer"],
        )

    if sigstore_bundle:
        try:
            verify_bundle_signature(
                archive_path, sigstore_bundle, oidc_identity, oidc_issuer
            )
        except VerificationError as e:
            raise click.ClickException(f"Signature verification failed: {e}") from e

    with tempfile.TemporaryDirectory(prefix="stax_archive_") as tmpdir:
        with zipfile.ZipFile(archive_path, "r") as zf:
            zf.extractall(tmpdir)

        tmp_path = Path(tmpdir)
        manifest_path = tmp_path / "manifest.yaml"
        if not manifest_path.exists():
            raise click.ClickException("manifest.yaml not found at bundle root")

        manifest = load_manifest_from_path(manifest_path)

        templates_dir = tmp_path / "templates"
        if templates_dir.exists() and templates_dir.is_dir():
            template_files = sorted(templates_dir.glob("*.yaml"))
            if template_files:
                lint_errors = _run_cfn_lint(template_files)
                if lint_errors:
                    raise click.ClickException(
                        "cfn-lint found issues:\n" + "\n".join(lint_errors)
                    )
            else:
                raise click.ClickException("No templates found")
        else:
            raise click.ClickException("No templates found")

        cfn = boto3.client("cloudformation")
        for resource in manifest.resources:
            if resource.deploy_method == DeployMethod.STACK_SET:
                # Only handle stack sets for now
                _deploy_stack_set(cfn, tmp_path, manifest.region, resource, prefix)


if __name__ == "__main__":
    main()


def _stack_set_exists(cfn, stack_set_name):
    try:
        cfn.describe_stack_set(StackSetName=stack_set_name, CallAs="SELF")
        return True
    except ClientError as exc:
        code = exc.response.get("Error", {}).get("Code")
        if code != "StackSetNotFoundException":
            raise
    return False


def _get_target_spec(resource):
    targets = resource.deployment_targets
    target_spec = {}
    if targets.organizational_units:
        target_spec["OrganizationalUnitIds"] = targets.organizational_units
    if targets.accounts:
        # Uggh this API is horrible. Can't just specify accounts, despite what the API
        # docs say. Need to specify an OU the account ID is in, then use the
        # INTERSECTION filter type and then specify the account IDs.
        target_spec["Accounts"] = targets.accounts
        target_spec["AccountFilterType"] = "INTERSECTION"
        target_spec["OrganizationalUnitIds"] = targets.organizational_units
    return target_spec


def _deploy_stack_set(
    cfn,
    bundle_root: Path,
    default_region: str,
    resource,
    prefix: str,
) -> None:
    stack_set_name = f"{prefix}-{resource.name}"
    template_path = bundle_root / resource.resource_file
    if not template_path.exists():
        raise click.ClickException(
            f"Template not found for resource '{resource.name}': {template_path}"
        )

    with template_path.open("r", encoding="utf-8") as fh:
        template_body = fh.read()

    parameters = [
        {
            "ParameterKey": p.parameter_key,
            "ParameterValue": p.parameter_value,
        }
        for p in getattr(resource, "parameters", [])
    ]

    target_spec = _get_target_spec(resource)
    regions = resource.regions or [default_region]

    if _stack_set_exists(cfn, stack_set_name):
        click.echo(f"Existing stack set found: {stack_set_name} - updating")
        try:
            _update_stack_set(
                cfn, stack_set_name, template_body, parameters, target_spec, regions
            )
        except ClientError as exc:
            if (
                exc.response.get("Error", {}).get("Code")
                != "StackInstanceNotFoundException"
            ):
                raise

            click.echo(
                "Updating a stack with no stack instances - ignoring and "
                "proceeding to create stack instances"
            )

    else:
        click.echo(f"No existing stack set found: {stack_set_name} - creating")
        _create_stack_set(cfn, stack_set_name, template_body, parameters)

    click.echo(f"Deploying stack set instances: {stack_set_name}")
    attempt = 0
    success = False
    while attempt < 30 and not success:
        try:
            cfn.create_stack_instances(
                StackSetName=stack_set_name,
                DeploymentTargets=target_spec,
                Regions=regions,
                CallAs="SELF",
                OperationPreferences={
                    "FailureTolerancePercentage": 30,
                    "MaxConcurrentPercentage": 100,
                    "RegionConcurrencyType": "SEQUENTIAL",
                },
            )
            success = True
        except ClientError as exc:
            code = exc.response.get("Error", {}).get("Code")
            if code != "OperationInProgressException":
                raise
            attempt += 1
            click.echo("Waiting for stack set operation to complete...")
            time.sleep(10)
    if not success:
        raise click.ClickException(
            "Timed out waiting for stack set operation to complete - stacks not updated"
        )


def _run_cfn_lint(template_files: list[Path]) -> list[str]:
    errors: list = []

    for path in template_files:
        matches = cfnlint.lint_file(path)
        errors.extend(matches)
    return errors


def _create_stack_set(cfn, stack_set_name, template_body, parameters):
    cfn.create_stack_set(
        StackSetName=stack_set_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
        PermissionModel="SERVICE_MANAGED",
        AutoDeployment={
            "Enabled": True,
            "RetainStacksOnAccountRemoval": True,
        },
        CallAs="SELF",
    )


def _update_stack_set(
    cfn, stack_set_name, template_body, parameters, target_spec, regions
):
    cfn.update_stack_set(
        StackSetName=stack_set_name,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"],
        PermissionModel="SERVICE_MANAGED",
        AutoDeployment={
            "Enabled": True,
            "RetainStacksOnAccountRemoval": True,
        },
        CallAs="SELF",
        DeploymentTargets=target_spec,
        Regions=regions,
    )
