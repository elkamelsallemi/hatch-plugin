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
        files_to_exclude = ["README.md", "LICENSE.txt"]  # Specify files to exclude
        excluded_files = set()

        for included_file in build_data.get("force_include", {}).copy():
            if any(included_file.endswith(f) for f in files_to_exclude):
                print(f"Excluding file: {included_file}")
                excluded_files.add(included_file)

        # Remove the excluded files from the "force_include" list
        for excluded_file in excluded_files:
            build_data["force_include"].pop(excluded_file, None)

    def finalize(self, version: str, build_data: dict[str, Any], artifact_path: str) -> None:  # noqa: ARG002
        """Called during the finalization phase of the build"""
        print("Hello, World! Finalization phase.")