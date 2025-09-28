"""
Server components to orchestrate plugins.

Components for starting and operating the stashhouse server.
The server orchestrates the starting and stopping of plugins,
which accept file uploads and places them appropriately.
"""

import contextlib
import logging
import multiprocessing
import pathlib
from types import TracebackType
from typing import Self, Any, NamedTuple, TYPE_CHECKING

from . import plugin

if TYPE_CHECKING:
    # noinspection PyProtectedMember
    from importlib.metadata import EntryPoint

logger = logging.getLogger(__name__)


class ServerOptions(NamedTuple):
    """
    Global server options.

    Server options are available to all plugins. However,
    plugins may offer configuration options to override
    these while using server options as fallback.

    Attributes:
        host: Address plugins should bind to.
        plugins: List of plugins to load.
        log_level: Minimum log level to log.
        directory: Path to store files.
    """

    host: str = "127.0.0.1"
    plugins: list[str] = []
    log_level: int = logging.INFO
    directory: pathlib.Path = pathlib.Path("data")


class Server:
    """
    Orchestrates plugin launches.

    The server centrally manages all running plugins
    such that they all start and stop at the same
    time. The server itself is a ContextManager;
    however, the start and stop methods may
    alternatively be called directly. An "exited"
    attribute is exposed, which plugins are expected
    to occasionally check to determine if they should
    shut down. Plugin options apply to specific plugins
    and may be sent as keyword arguments where values
    are a dictionary of values representing keyword
    arguments to initialize plugins with.

    Attributes:
        options: Server options to apply globally.
        exited: Whether plugins should stop.
        plugin_options: Options to apply at the plugin level.
        _plugins: An exit stack to clean up the server.
        _processes: List of all processes launched.
    """

    def __init__(self, options: ServerOptions | None = None, **plugin_options):
        """
        Initializes the server.

        Args:
        options: Server options to apply globally.
        plugin_options: Options to apply at the plugin level.
        """

        self.options = options
        if self.options is None:
            self.options = ServerOptions()

        self.exited = multiprocessing.Event()
        self.plugin_options = plugin_options
        self._plugins: contextlib.ExitStack = contextlib.ExitStack()
        self._processes: list[multiprocessing.Process] = []

    def _load_plugin(self, plugin_entry: "EntryPoint") -> None:
        """
        Launch a plugin.

        Given a plugin entry, launch it in a new process.
        Processes are used to separate the memory spaces
        while retaining the ability for plugins to launch
        their own threads, leaving the option to leverage
        asyncio or threads rather than forcing it.

        Args:
            plugin_entry: An entrypoint to a plugin.Plugin instance.
        """

        plugin_options: plugin.PluginOptions | dict[str, Any] = self.plugin_options.get(
            plugin_entry.name, {}
        )

        plugin_enabled: bool = plugin_options.get("enable", True)
        if not plugin_enabled:
            logger.info("Plugin disabled: %s", plugin_entry.name)
            return

        logger.info("Loading plugin: %s", plugin_entry.name)
        # fmt: off
        plugin_process: multiprocessing.Process = plugin.run_server_plugin(
            plugin_entry, self.options, exited=self.exited,
            log_level=self.options.log_level, **plugin_options
        )
        plugin_process.start()
        self._processes.append(plugin_process)
        self._plugins.callback(plugin_process.join)

    def start(self) -> None:
        """
        Start the server and all enabled plugins.

        Identifies all plugins through finding all entry
        points in the group "stashhouse.plugins.server".
        It is expected that the value maps to a class
        conforming to the plugin.Plugin protocol.
        """

        try:
            for plugin_entry in plugin.find_server_plugins():
                if plugin_entry.name not in self.options.plugins:
                    continue

                self._load_plugin(plugin_entry)
        except:
            logger.exception("Failed to load one or more plugins. Shutting down.")
            self.stop()
            raise

    def stop(self) -> None:
        """
        Stop the server and all running plugins.

        Sets the "exited" attribute, signaling plugins
        to stop. Plugins are not guaranteed to stop
        immediately, nor at all, although they should.
        Once set, all running plugin processes are
        joined until they all stop.
        """

        self.exited.set()
        self._plugins.close()

    def join(self, timeout: float | None = None) -> None:
        """
        Joins all processes.

        For each process, block until the process finishes or until
        timeout seconds have elapsed. The timeout is per process
        and not across all processes. Joining processes can help
        clean up zombie processes if one were to stop.

        Args:
            timeout: Maximum number of seconds to block per process.
        """

        for process in self._processes:
            process.join(timeout)

    def __enter__(self) -> Self:
        """
        Start the server and all enabled plugins.

        See also:
            start: Start the server, and all enabled plugins.

        Returns:
            The server instance.
        """

        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        """
        Stop the server and all running plugins.

        Args:
            exc_type: Exception class if an exception occurred.
            exc_val: Exception instance if an exception occurred.
            exc_tb: Exception traceback if an exception occurred.
        """

        self.stop()


__all__ = ("Server", "ServerOptions")
