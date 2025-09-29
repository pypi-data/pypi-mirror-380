# GitHub Actions Deploy

A Python library for automating Google Cloud Run deployments in GitHub Actions with VPC Service Controls support and automatic PR commenting.

## Features

- 🚀 **VPC-SC Support**: Handles VPC Service Controls constraints with async builds
- 💬 **Auto PR Comments**: Posts build started and completion comments with service URLs
- 🐳 **Docker Integration**: Seamless container building and deployment
- ⚡ **Fast & Reliable**: Optimized for CI/CD environments
- 🔧 **Highly Configurable**: Support for custom timeouts, secrets, and environments

## Quick Start

### Installation

```bash
pip install github-actions-deploy
```

### GitHub Actions Workflow

Copy the template from `templates/pr-preview.yml` and customize:

```yaml
- name: Deploy using github-actions-deploy
  env:
    GCP_PROJECT: your-project-id
    GCP_REGION: us-central1
    SERVICE_NAME: "your-service-pr-${{ steps.pr_number.outputs.number }}"
    IMAGE_TAG: "gcr.io/your-project/your-service:pr-${{ steps.pr_number.outputs.number }}-${{ github.sha }}"
    GITHUB_REPOSITORY: ${{ github.repository }}
    GITHUB_HEAD_REF: ${{ github.head_ref }}
    PR_NUMBER: ${{ steps.pr_number.outputs.number }}
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    gha-deploy \
      --project-id "$GCP_PROJECT" \
      --region "$GCP_REGION" \
      --service-name "$SERVICE_NAME" \
      --image-tag "$IMAGE_TAG" \
      --repository "$GITHUB_REPOSITORY" \
      --pr-number "$PR_NUMBER" \
      --branch-name "$GITHUB_HEAD_REF" \
      --secrets "API_KEY=api-key-secret:latest"
```

## Key Components

### VPC Service Controls (VPC-SC) Support

The library automatically detects CI environments and uses async builds to avoid VPC-SC log streaming restrictions:

```python
from github_actions_deploy import CloudRunDeployer, DeploymentConfig

config = DeploymentConfig.from_environment()
deployer = CloudRunDeployer(config)

# Automatically handles VPC-SC async builds in CI
service_url = deployer.deploy(branch_name="main")
```

### PR Status Comments

Automatically posts comments showing:

1. **Build Started**: Progress indicators and estimated time
2. **Deployment Complete**: Service URLs and quick access links
3. **Deployment Failed**: Error details and troubleshooting steps

### Configuration

The library uses environment variables or can be configured programmatically:

```python
config = DeploymentConfig(
    project_id="your-project",
    region="us-central1",
    service_name="your-service",
    repository="owner/repo",
    pr_number=123,
    use_vpc_sc_async=True  # Enables VPC-SC async build mode
)
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GCP_PROJECT` | Google Cloud Project ID | Yes |
| `GCP_REGION` | Google Cloud Region | No (default: us-central1) |
| `SERVICE_NAME` | Cloud Run service name | Yes |
| `GITHUB_REPOSITORY` | GitHub repository (owner/repo) | Yes |
| `GITHUB_HEAD_REF` | Git branch name | Yes |
| `PR_NUMBER` | Pull request number | For PR deployments |
| `GITHUB_TOKEN` | GitHub token for API access | For PR comments |

## Templates

The package includes ready-to-use GitHub Actions templates:

- `templates/pr-preview.yml`: PR preview deployments with comments
- `templates/production-deploy.yml`: Production deployments

## Prerequisites

1. **Google Cloud Setup**:
   - Service account with Cloud Run and Cloud Build permissions
   - VPC Service Controls configured (if applicable)
   - Secret Manager for API keys

2. **GitHub Setup**:
   - Repository secrets for `GCP_SA_KEY`
   - `pull-requests: write` permission for PR comments

## Advanced Usage

### Custom Secrets

```bash
gha-deploy --secrets "API_KEY=api-key:latest,DB_PASSWORD=db-pass:latest"
```

### Skip PR Comments

```bash
gha-deploy --no-comments
```

### Custom Timeout

```bash
gha-deploy --timeout-minutes 20
```

## Development

```bash
git clone https://github.com/jleechanorg/ai_universe
cd packages/github-actions-deploy
pip install -e ".[dev]"
pytest
```

## License

MIT License - see LICENSE file for details.