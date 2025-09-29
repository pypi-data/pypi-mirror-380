"""Configuration management for deployment automation."""

import os
from typing import Optional
from pydantic import BaseModel, Field


class DeploymentConfig(BaseModel):
    """Configuration for deployment automation."""

    # Google Cloud Configuration
    project_id: str = Field(..., description="Google Cloud Project ID")
    region: str = Field(default="us-central1", description="Google Cloud Region")

    # Service Configuration
    service_name: str = Field(..., description="Cloud Run service name")
    image_tag: Optional[str] = Field(default=None, description="Container image tag")

    # GitHub Configuration
    repository: str = Field(..., description="GitHub repository (owner/repo)")
    pr_number: Optional[int] = Field(default=None, description="Pull request number")

    # Environment Detection
    is_ci: bool = Field(default=False, description="Running in CI environment")
    is_github_actions: bool = Field(default=False, description="Running in GitHub Actions")

    # Build Configuration
    timeout_minutes: int = Field(default=15, description="Build timeout in minutes")
    use_vpc_sc_async: bool = Field(default=True, description="Use VPC-SC async build mode")

    @classmethod
    def from_environment(cls) -> "DeploymentConfig":
        """Create configuration from environment variables."""
        return cls(
            project_id=os.environ["GCP_PROJECT"],
            region=os.environ.get("GCP_REGION", "us-central1"),
            service_name=os.environ["SERVICE_NAME"],
            image_tag=os.environ.get("IMAGE_TAG"),
            repository=os.environ["GITHUB_REPOSITORY"],
            pr_number=int(os.environ["PR_NUMBER"]) if os.environ.get("PR_NUMBER") else None,
            is_ci=os.environ.get("CI", "").lower() == "true",
            is_github_actions=os.environ.get("GITHUB_ACTIONS", "").lower() == "true",
            timeout_minutes=int(os.environ.get("DEPLOYMENT_TIMEOUT_MINUTES", "15")),
            use_vpc_sc_async=os.environ.get("USE_VPC_SC_ASYNC", "true").lower() == "true",
        )

    @property
    def should_use_async_build(self) -> bool:
        """Determine if async build should be used based on environment."""
        return self.use_vpc_sc_async and (self.is_ci or self.is_github_actions)

    @property
    def service_url_base(self) -> str:
        """Generate the expected service URL base."""
        # Cloud Run URL format: https://SERVICE-PROJECT_HASH.REGION.run.app
        return f"https://{self.service_name}-.*\\.{self.region}\\.run\\.app"