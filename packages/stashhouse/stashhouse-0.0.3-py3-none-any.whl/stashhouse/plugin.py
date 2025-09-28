"""
Plugin execution utilities.
"""

import argparse
import logging
import multiprocessing
from importlib.metadata import entry_points
from typing import (
    Protocol,
    runtime_checkable,
    TypedDict,
    NotRequired,
    Unpack,
    TYPE_CHECKING,
    Generator,
    Callable,
)

if TYPE_CHECKING:
    from . import server

    # noinspection PyProtectedMember
    from importlib.metadata import EntryPoint, EntryPoints


class PluginOptions(TypedDict, total=False):
    """
    Plugin options.

    A plugin may optionally offer the "enable" option
    to designate whether a plugin should be enabled or not.
    If a plugin offers it, it must be a boolean. Plugins
    may offer additional plugin options.
    """

    enable: NotRequired[bool]


# pylint: disable=too-few-public-methods
@runtime_checkable
class Plugin(Protocol):
    """
    Defines method headers required for plugins.
    """

    # noinspection PyUnusedLocal
    def __init__(
        self,
        server_options: "server.ServerOptions",
        exited: multiprocessing.Event,
        **kwargs: Unpack[PluginOptions],
    ) -> None:
        """
        Initialize the plugin.

        Args:
            server_options: Globally available server options.
            exited: Whether the plugin should exit.
            **kwargs: Plugin options.
        """
        self.server_options = server_options
        self.exited = exited

    def run(self) -> None:
        """
        Start the plugin.
        """


PluginArgumentRegistrar = Callable[[str, argparse.ArgumentParser], None]
PluginArgumentParser = Callable[[str, argparse.Namespace], PluginOptions]

logger = logging.getLogger(__name__)


def find_server_plugins() -> Generator["EntryPoint", None, None]:
    """
    Identifies server plugin entry points.

    Yields:
        An entry point pointing to instances of Plugin.
    """

    yield from entry_points(group="stashhouse.plugins.server")


def find_cli_register_plugins() -> "EntryPoints":
    """
    Identifies CLI register plugins.

    A PluginArgumentRegistrar represents a callable that accepts
    a string plugin name and an argument parser with the
    expectation that it will register arguments as required to
    the provided argument parser.

    Yields:
        An entry point pointing to a PluginArgumentRegistrar.
    """

    return entry_points(group="stashhouse.plugins.cli.register")


def find_cli_parse_plugins() -> "EntryPoints":
    """
    Identifies CLI parser plugins.

    A PluginArgumentParser represents a callable that accepts
    a string plugin name and an argparse.Namespace with
    the expectation that it will return a dictionary of
    plugin options extracted from the namespace.

    Yields:
        An entry point pointing to a PluginArgumentParser.
    """
    return entry_points(group="stashhouse.plugins.cli.parse")


def _run_server_plugin(
    plugin: "EntryPoint", *args, log_level: int = logging.INFO, **kwargs
) -> None:
    """
    Executes a plugin.

    Exists to enable execution with multiprocessing while
    preventing excessive imports into the main process.

    Args:
        plugin: Entry point pointing to a Plugin.
        *args: Arguments to pass to the Plugin initializer.
        log_level: Minimum level to log.
        **kwargs: Keyword arguments to pass to the Plugin initializer.
    """

    logging.basicConfig(level=log_level)
    plugin_instance: Plugin = plugin.load()(*args, **kwargs)

    try:
        plugin_instance.run()
    except KeyboardInterrupt:
        kwargs["exited"].set()
    except:
        logger.exception("Shutting down plugin due to exception: %s", plugin.name)
        raise


def run_server_plugin(*args, **kwargs) -> multiprocessing.Process:
    """
    Creates a multiprocessing process to execute a plugin.

    Args:
        *args: Arguments to pass to _run_server_plugin.
        **kwargs: Keyword arguments to pass to _run_server_plugin.

    Returns:
        A multiprocessing process that when started, executes the plugin.
    """

    return multiprocessing.Process(target=_run_server_plugin, args=args, kwargs=kwargs)


__all__ = ("PluginOptions", "Plugin", "find_server_plugins", "run_server_plugin")
