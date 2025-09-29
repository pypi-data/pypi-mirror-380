"""Hooks for the hatch-webassets plugin."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hatchling.plugin import hookimpl

from hatch_webassets.hook import WebassetsBuildHook

if TYPE_CHECKING:
    from hatchling.builders.config import BuilderConfig
    from hatchling.builders.hooks.plugin.interface import BuildHookInterface


@hookimpl
def hatch_register_build_hook() -> type[BuildHookInterface[BuilderConfig]]:
    """Register the build hook.

    Returns:
        The build hook.
    """
    return WebassetsBuildHook
