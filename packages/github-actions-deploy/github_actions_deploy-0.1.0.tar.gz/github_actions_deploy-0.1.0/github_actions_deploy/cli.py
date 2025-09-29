"""Command-line interface for GitHub Actions deployment automation."""

import os
import sys
import click
from .config import DeploymentConfig
from .deployer import CloudRunDeployer


@click.command()
@click.option("--project-id", envvar="GCP_PROJECT", required=True, help="Google Cloud Project ID")
@click.option("--region", envvar="GCP_REGION", default="us-central1", help="Google Cloud Region")
@click.option("--service-name", envvar="SERVICE_NAME", required=True, help="Cloud Run service name")
@click.option("--image-tag", envvar="IMAGE_TAG", help="Container image tag")
@click.option("--repository", envvar="GITHUB_REPOSITORY", required=True, help="GitHub repository (owner/repo)")
@click.option("--pr-number", envvar="PR_NUMBER", type=int, help="Pull request number")
@click.option("--branch-name", envvar="GITHUB_HEAD_REF", required=True, help="Git branch name")
@click.option("--dockerfile-path", default=".", help="Path to Dockerfile directory")
@click.option("--timeout-minutes", envvar="DEPLOYMENT_TIMEOUT_MINUTES", type=int, default=15, help="Deployment timeout")
@click.option("--secrets", help="Comma-separated secrets (ENV_VAR=secret_name:version)")
@click.option("--no-comments", is_flag=True, help="Skip GitHub PR comments")
@click.option("--vpc-sc-async/--no-vpc-sc-async", default=True, help="Use VPC-SC async build mode")
def main(
    project_id: str,
    region: str,
    service_name: str,
    image_tag: str,
    repository: str,
    pr_number: int,
    branch_name: str,
    dockerfile_path: str,
    timeout_minutes: int,
    secrets: str,
    no_comments: bool,
    vpc_sc_async: bool
):
    """Deploy to Google Cloud Run with GitHub Actions integration."""

    # Parse secrets
    secret_dict = {}
    if secrets:
        for secret_pair in secrets.split(","):
            if "=" in secret_pair:
                env_var, secret_ref = secret_pair.split("=", 1)
                secret_dict[env_var.strip()] = secret_ref.strip()

    # Create configuration
    config = DeploymentConfig(
        project_id=project_id,
        region=region,
        service_name=service_name,
        image_tag=image_tag,
        repository=repository,
        pr_number=pr_number,
        is_ci=os.environ.get("CI", "").lower() == "true",
        is_github_actions=os.environ.get("GITHUB_ACTIONS", "").lower() == "true",
        timeout_minutes=timeout_minutes,
        use_vpc_sc_async=vpc_sc_async,
    )

    # Deploy
    deployer = CloudRunDeployer(config)
    try:
        service_url = deployer.deploy(
            branch_name=branch_name,
            dockerfile_path=dockerfile_path,
            secrets=secret_dict,
            post_comments=not no_comments
        )
        click.echo(f"✅ Deployment successful: {service_url}")
        sys.exit(0)
    except Exception as e:
        click.echo(f"❌ Deployment failed: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()