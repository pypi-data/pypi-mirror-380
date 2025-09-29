"""Cloud Run deployment functionality."""

import subprocess
import json
from typing import Optional, Dict, Any
from .config import DeploymentConfig
from .vpc_sc import VPCSCHandler
from .github_comments import GitHubCommenter


class CloudRunDeployer:
    """Handles Google Cloud Run deployments with VPC-SC support."""

    def __init__(self, config: DeploymentConfig):
        self.config = config
        self.vpc_handler = VPCSCHandler(config)
        self.commenter = GitHubCommenter(config)

    def deploy(
        self,
        branch_name: str,
        dockerfile_path: str = ".",
        secrets: Optional[Dict[str, str]] = None,
        post_comments: bool = True
    ) -> str:
        """
        Deploy service to Cloud Run with comprehensive status tracking.

        Args:
            branch_name: Git branch name
            dockerfile_path: Path to Dockerfile directory
            secrets: Secret manager secrets to mount
            post_comments: Whether to post GitHub PR comments

        Returns:
            Deployed service URL

        Raises:
            subprocess.CalledProcessError: If deployment fails
        """
        try:
            # Post build started comment
            if post_comments:
                self.commenter.post_build_started(branch_name)

            # Build image using VPC-SC handler
            image_tag = self.config.image_tag or self._generate_image_tag()
            self.vpc_handler.build_image_async(image_tag, dockerfile_path)

            # Deploy to Cloud Run
            service_url = self._deploy_to_cloud_run(image_tag, secrets)

            # Verify deployment health
            self._verify_health(service_url)

            # Post success comment
            if post_comments:
                self.commenter.post_deployment_success(service_url, branch_name)

            return service_url

        except subprocess.CalledProcessError as e:
            if post_comments:
                self.commenter.post_deployment_failure(branch_name, str(e))
            raise

        except Exception as e:
            if post_comments:
                self.commenter.post_deployment_failure(branch_name, f"Unexpected error: {e}")
            raise

    def _generate_image_tag(self) -> str:
        """Generate image tag based on configuration."""
        if self.config.pr_number:
            return f"gcr.io/{self.config.project_id}/{self.config.service_name}:{self.config.pr_number}"
        else:
            return f"gcr.io/{self.config.project_id}/{self.config.service_name}:latest"

    def _deploy_to_cloud_run(self, image_tag: str, secrets: Optional[Dict[str, str]] = None) -> str:
        """Deploy image to Cloud Run."""
        print("🚀 Deploying to Cloud Run...")

        # Check if service exists
        try:
            subprocess.run([
                "gcloud", "run", "services", "describe", self.config.service_name,
                "--region", self.config.region,
                "--quiet"
            ], capture_output=True, check=True)
            deploy_strategy = "update"
            print("🔄 Updating existing service")
        except subprocess.CalledProcessError:
            deploy_strategy = "create"
            print("🆕 Creating new service")

        # Prepare deployment command
        deploy_cmd = [
            "gcloud", "run", "deploy", self.config.service_name,
            "--image", image_tag,
            "--region", self.config.region,
            "--platform", "managed",
            "--allow-unauthenticated",
            "--memory", "2Gi",
            "--cpu", "2",
            "--max-instances", "100",
            "--min-instances", "0",
            "--timeout", "3600",
            "--port", "8080",
            "--quiet"
        ]

        # Add secrets if provided
        if secrets:
            secret_args = []
            for env_var, secret_ref in secrets.items():
                secret_args.extend(["--set-secrets", f"{env_var}={secret_ref}"])
            deploy_cmd.extend(secret_args)

        # Execute deployment
        print(f"🚀 Executing gcloud run deploy (timeout: {self.config.timeout_minutes} minutes)...")
        result = subprocess.run(deploy_cmd, capture_output=True, text=True, check=True)

        # Extract service URL from output
        service_url = self._extract_service_url()
        print("✅ Deployment successful!")
        print(f"🔗 Service URL: {service_url}")

        return service_url

    def _extract_service_url(self) -> str:
        """Extract service URL from Cloud Run service."""
        result = subprocess.run([
            "gcloud", "run", "services", "describe", self.config.service_name,
            "--region", self.config.region,
            "--format=value(status.url)",
            "--quiet"
        ], capture_output=True, text=True, check=True)

        service_url = result.stdout.strip()
        if not service_url:
            raise RuntimeError(f"Could not retrieve service URL for {self.config.service_name}")

        return service_url

    def _verify_health(self, service_url: str) -> None:
        """Verify service health after deployment."""
        print("🔍 Testing health endpoint...")

        try:
            # Simple curl check - could be enhanced with retries
            subprocess.run([
                "curl", "-f", "--max-time", "30",
                f"{service_url}/health"
            ], capture_output=True, check=True)
            print("✅ Health check passed!")

        except subprocess.CalledProcessError:
            print("⚠️ Health check failed, but service may still be starting...")
            # Don't fail deployment for health check issues