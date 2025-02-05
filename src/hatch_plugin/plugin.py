from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from python_minifier import minify

class MinifyBuildHook(BuildHookInterface):
    PLUGIN_NAME = "minifyer"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.builder = self.build_config.builder

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """Called during the initialization phase of the build"""
        print("Hello, World! Initialization phase.")
        project_name = self.build_config.name
        
        # Print the project name for debugging
        print(f"Project name must start with 'monorepo-', but got: {project_name}")

    def finalize(self, version: str, build_data: dict[str, Any], artifact_path: str) -> None:  # noqa: ARG002
        """Called during the finalization phase of the build"""
        print("Hello, World! Finalization phase.")