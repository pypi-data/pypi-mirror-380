"""Test configuration functionality."""

import os
import pytest
from github_actions_deploy.config import DeploymentConfig


def test_deployment_config_basic():
    """Test basic DeploymentConfig creation."""
    config = DeploymentConfig(
        project_id="test-project",
        service_name="test-service",
        repository="owner/repo"
    )

    assert config.project_id == "test-project"
    assert config.service_name == "test-service"
    assert config.repository == "owner/repo"
    assert config.region == "us-central1"  # default


def test_deployment_config_from_environment(monkeypatch):
    """Test creating config from environment variables."""
    monkeypatch.setenv("GCP_PROJECT", "env-project")
    monkeypatch.setenv("GCP_REGION", "us-west1")
    monkeypatch.setenv("SERVICE_NAME", "env-service")
    monkeypatch.setenv("GITHUB_REPOSITORY", "env-owner/env-repo")
    monkeypatch.setenv("PR_NUMBER", "42")
    monkeypatch.setenv("CI", "true")
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    config = DeploymentConfig.from_environment()

    assert config.project_id == "env-project"
    assert config.region == "us-west1"
    assert config.service_name == "env-service"
    assert config.repository == "env-owner/env-repo"
    assert config.pr_number == 42
    assert config.is_ci is True
    assert config.is_github_actions is True


def test_should_use_async_build():
    """Test async build detection logic."""
    # CI environment should use async
    config = DeploymentConfig(
        project_id="test",
        service_name="test",
        repository="test/test",
        is_ci=True,
        use_vpc_sc_async=True
    )
    assert config.should_use_async_build is True

    # GitHub Actions should use async
    config.is_ci = False
    config.is_github_actions = True
    assert config.should_use_async_build is True

    # Local development should not use async
    config.is_ci = False
    config.is_github_actions = False
    assert config.should_use_async_build is False

    # Disabled VPC-SC should not use async
    config.is_ci = True
    config.use_vpc_sc_async = False
    assert config.should_use_async_build is False