"""Entry point for the hatch-webassets plugin."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from hatchling.builders.config import BuilderConfig
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

if TYPE_CHECKING:
    from hatch_webassets.config import Config


class WebassetsBuildHook(BuildHookInterface[BuilderConfig]):
    """Build hook for webassets."""

    PLUGIN_NAME = "webassets"

    config: Config  # type: ignore[assignment]

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        """Initialize the build hook."""

    def finalize(self, version: str, build_data: Any, artifact_path: str) -> None:  # noqa: ANN401
        """Finalize the build hook."""
