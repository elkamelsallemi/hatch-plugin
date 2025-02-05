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
        project_name = self.metadata.name

        if not project_name.startswith("monorepo-"):
            raise ValueError(
                f"Invalid project name: '{project_name}'. "
                "Project name must start with 'monorepo-'."
            )

        print(f"Hello, World! Initialization phase. Project name: {project_name}")
        print("Hello, World! Initialization phase.")


    def finalize(self, version: str, build_data: dict[str, Any], artifact_path: str) -> None:  # noqa: ARG002
        """Called during the finalization phase of the build"""
        print("Hello, World! Finalization phase.")