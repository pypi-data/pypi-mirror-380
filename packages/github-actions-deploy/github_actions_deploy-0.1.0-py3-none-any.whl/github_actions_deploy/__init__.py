"""
GitHub Actions Deploy - Deployment automation with VPC-SC support and PR commenting.

A Python library for automating deployments in GitHub Actions with:
- VPC Service Controls (VPC-SC) support
- Automatic PR status comments
- Google Cloud Run deployment
- Docker image building with async support
- Comprehensive error handling and logging
"""

from .deployer import CloudRunDeployer
from .github_comments import GitHubCommenter
from .config import DeploymentConfig
from .vpc_sc import VPCSCHandler

__version__ = "0.1.0"

__all__ = [
    "CloudRunDeployer",
    "GitHubCommenter",
    "DeploymentConfig",
    "VPCSCHandler",
    "__version__",
]