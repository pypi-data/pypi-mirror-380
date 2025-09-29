"""GitHub PR commenting functionality for deployment automation."""

import os
import subprocess
from typing import Optional
from .config import DeploymentConfig


class GitHubCommenter:
    """Handles posting comments to GitHub PRs during deployment."""

    def __init__(self, config: DeploymentConfig, github_token: Optional[str] = None):
        self.config = config
        self.github_token = github_token or os.environ.get("GITHUB_TOKEN")
        self.github_sha = os.environ.get("GITHUB_SHA", "")
        self.github_run_id = os.environ.get("GITHUB_RUN_ID", "")
        self.github_server_url = os.environ.get("GITHUB_SERVER_URL", "https://github.com")

    def _run_gh_command(self, args: list[str]) -> str:
        """Run a GitHub CLI command."""
        env = os.environ.copy()
        if self.github_token:
            env["GH_TOKEN"] = self.github_token

        result = subprocess.run(
            ["gh"] + args,
            capture_output=True,
            text=True,
            env=env,
            check=True
        )
        return result.stdout.strip()

    def _get_commit_short(self) -> str:
        """Get short commit hash."""
        return self.github_sha[:7] if self.github_sha else "unknown"

    def _get_workflow_url(self) -> str:
        """Get GitHub Actions workflow URL."""
        if self.github_run_id:
            return f"{self.github_server_url}/{self.config.repository}/actions/runs/{self.github_run_id}"
        return f"{self.github_server_url}/{self.config.repository}/actions"

    def _get_commit_url(self) -> str:
        """Get commit URL."""
        if self.github_sha:
            return f"{self.github_server_url}/{self.config.repository}/commit/{self.github_sha}"
        return f"{self.github_server_url}/{self.config.repository}"

    def post_build_started(self, branch_name: str, estimated_minutes: str = "8-12") -> None:
        """Post a comment when build starts."""
        if not self.config.pr_number:
            return

        commit_short = self._get_commit_short()
        workflow_url = self._get_workflow_url()
        commit_url = self._get_commit_url()

        body = f"""## 🚀 Build Started

**Commit:** [`{commit_short}`]({commit_url})
**Branch:** `{branch_name}`
**Service:** `{self.config.service_name}`
**Workflow:** [View Progress]({workflow_url})

### 🔄 Build Steps:
- ✅ Environment setup
- ✅ Shared libraries built
- 🔄 **Docker image build** (VPC-SC async)
- ⏳ Cloud Run deployment
- ⏳ Health check verification

*Estimated time: {estimated_minutes} minutes*

🤖 *Auto-deployment in progress via GitHub Actions*"""

        self._run_gh_command([
            "pr", "comment", str(self.config.pr_number),
            "--body", body
        ])

    def post_deployment_success(self, service_url: str, branch_name: str) -> None:
        """Post a comment when deployment succeeds."""
        if not self.config.pr_number:
            return

        commit_short = self._get_commit_short()
        workflow_url = self._get_workflow_url()
        commit_url = self._get_commit_url()

        body = f"""## ✅ Deployment Complete!

**🎉 Your PR preview is ready!**

### 🔗 Quick Access:
| Service | URL |
|---------|-----|
| 🌐 **Preview App** | [{service_url}]({service_url}) |
| 🩺 **Health Check** | [{service_url}/health]({service_url}/health) |
| 📡 **MCP Endpoint** | [{service_url}/mcp]({service_url}/mcp) |

### 🔄 Completed Build Steps:
- ✅ Environment setup
- ✅ Shared libraries built
- ✅ **Docker image build** (VPC-SC async)
- ✅ Cloud Run deployment
- ✅ Health check verification

### 📋 Deployment Details:
- **Commit:** [`{commit_short}`]({commit_url})
- **Service:** `{self.config.service_name}`
- **Region:** `{self.config.region}`
- **Branch:** `{branch_name}`
- **Workflow:** [View Details]({workflow_url})

🤖 *Auto-deployed via GitHub Actions*"""

        self._run_gh_command([
            "pr", "comment", str(self.config.pr_number),
            "--body", body
        ])

    def post_deployment_failure(self, branch_name: str, error_message: Optional[str] = None) -> None:
        """Post a comment when deployment fails."""
        if not self.config.pr_number:
            return

        commit_short = self._get_commit_short()
        workflow_url = self._get_workflow_url()
        commit_url = self._get_commit_url()

        error_section = ""
        if error_message:
            error_section = f"""
### ❌ Error Details:
```
{error_message}
```
"""

        body = f"""## ❌ Deployment Failed

The deployment process encountered an error and could not complete.
{error_section}
### 📋 Details:
- **Commit:** [`{commit_short}`]({commit_url})
- **Service:** `{self.config.service_name}`
- **Branch:** `{branch_name}`
- **Workflow:** [View Logs]({workflow_url})

### 🔍 Next Steps:
1. Check the [workflow logs]({workflow_url}) for details
2. Review any error messages in the deployment step
3. Push a new commit to retry the deployment

🤖 *Auto-deployment failed via GitHub Actions*"""

        self._run_gh_command([
            "pr", "comment", str(self.config.pr_number),
            "--body", body
        ])

    def post_deployment_unknown(self, branch_name: str) -> None:
        """Post a comment when deployment status is unknown."""
        if not self.config.pr_number:
            return

        commit_short = self._get_commit_short()
        workflow_url = self._get_workflow_url()
        commit_url = self._get_commit_url()

        body = f"""## ⚠️ Deployment Status Unknown

The deployment process completed, but the service URL could not be retrieved.

### 📋 Details:
- **Commit:** [`{commit_short}`]({commit_url})
- **Service:** `{self.config.service_name}`
- **Region:** `{self.config.region}`
- **Workflow:** [View Details]({workflow_url})

Please check the [Google Cloud Console](https://console.cloud.google.com/run?project={self.config.project_id}) for more details.

🤖 *Auto-deployed via GitHub Actions*"""

        self._run_gh_command([
            "pr", "comment", str(self.config.pr_number),
            "--body", body
        ])