"""VPC Service Controls handling for Google Cloud Build."""

import subprocess
import time
from typing import Optional
from .config import DeploymentConfig


class VPCSCHandler:
    """Handles VPC Service Controls constraints during deployment."""

    def __init__(self, config: DeploymentConfig):
        self.config = config

    def build_image_async(
        self,
        image_tag: str,
        dockerfile_path: str = ".",
        timeout_minutes: Optional[int] = None
    ) -> str:
        """
        Build Docker image using async mode to avoid VPC-SC log streaming issues.

        Args:
            image_tag: Full image tag (e.g., gcr.io/project/image:tag)
            dockerfile_path: Path to Dockerfile directory
            timeout_minutes: Build timeout (uses config default if not provided)

        Returns:
            Service URL after successful deployment

        Raises:
            subprocess.CalledProcessError: If build or deployment fails
        """
        timeout = timeout_minutes or self.config.timeout_minutes

        if self.config.should_use_async_build:
            return self._build_async(image_tag, dockerfile_path, timeout)
        else:
            return self._build_sync(image_tag, dockerfile_path)

    def _build_async(self, image_tag: str, dockerfile_path: str, timeout_minutes: int) -> str:
        """Build using async mode with status polling."""
        print(f"🐳 Building container image asynchronously (CI environment - avoids VPC-SC log streaming issues)...")

        # Start async build and capture operation ID
        result = subprocess.run([
            "gcloud", "builds", "submit", dockerfile_path,
            "--tag", image_tag,
            "--async",
            "--format=value(name)",
            "--quiet"
        ], capture_output=True, text=True, check=True)

        build_operation = result.stdout.strip()
        print(f"📋 Build operation: {build_operation}")

        # Wait for build completion using status polling
        print(f"⏳ Waiting for build completion (timeout: {timeout_minutes} minutes)...")
        start_time = time.time()
        timeout_seconds = timeout_minutes * 60

        while True:
            # Check build status
            try:
                result = subprocess.run([
                    "gcloud", "builds", "describe", build_operation,
                    "--format=value(status)",
                    "--quiet"
                ], capture_output=True, text=True, check=False)

                status = result.stdout.strip() if result.returncode == 0 else "UNKNOWN"
                print(f"Build status: {status}")

                if status == "SUCCESS":
                    print("✅ Build completed successfully")
                    break
                elif status in ["FAILURE", "CANCELLED", "TIMEOUT"]:
                    raise subprocess.CalledProcessError(1, "gcloud builds submit", f"Build failed with status: {status}")
                elif time.time() - start_time > timeout_seconds:
                    raise subprocess.CalledProcessError(1, "gcloud builds submit", f"Build timed out after {timeout_minutes} minutes")
                else:
                    print("Build in progress...")
                    time.sleep(10)

            except subprocess.CalledProcessError as e:
                if "not found" in str(e) or e.returncode != 0:
                    raise subprocess.CalledProcessError(1, "gcloud builds submit", f"Failed to check build status: {e}")

        return image_tag

    def _build_sync(self, image_tag: str, dockerfile_path: str) -> str:
        """Build using synchronous mode (local development)."""
        print(f"🐳 Building container image synchronously...")

        subprocess.run([
            "gcloud", "builds", "submit", dockerfile_path,
            "--tag", image_tag,
            "--quiet"
        ], check=True)

        print("✅ Build completed successfully")
        return image_tag