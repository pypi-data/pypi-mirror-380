from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from watchfiles import Change, awatch

from raito.utils import loggers

from .loader import RouterLoader
from .parser import RouterParser

if TYPE_CHECKING:
    from collections.abc import Generator

    from aiogram import Dispatcher

    from raito.utils.types import StrOrPath

__all__ = ("RouterManager",)


class RouterManager:
    """Manages multiple routers and file watching."""

    def __init__(self, dispatcher: Dispatcher) -> None:
        """Initialize the RouterManager.

        :param dispatcher: Aiogram dispatcher instance
        :type dispatcher: Dispatcher
        """
        self.dispatcher = dispatcher

        self.loaders: dict[str, RouterLoader] = {}

    def resolve_paths(self, directory: StrOrPath) -> Generator[StrOrPath]:  # pyright: ignore [reportInvalidTypeArguments]
        """Recursively resolve all router paths in a directory.

        Scans the given directory recursively for Python files that can contain routers.
        Ignores files and directories starting with underscore `_`

        :param directory: Directory to scan for router files
        :type directory: StrOrPath
        :yield: Path objects for router files found in the directory
        :rtype: Generator[StrOrPath, None, None]
        """
        dir_path = Path(directory)

        for item in dir_path.iterdir():
            if item.name.startswith("_"):  # ignore files with prefix _
                continue

            if item.is_file() and item.suffix == ".py":
                yield item
            elif item.is_dir():
                yield from self.resolve_paths(item)

    async def load_routers(self, directory: StrOrPath) -> None:
        """Load all routers from a directory.

        Scans the directory for Python files containing routers, extracts them,
        handles name conflicts by adding unique suffixes, and registers them
        with the dispatcher.

        :param directory: Directory containing router files
        :type directory: StrOrPath
        :raises AttributeError: If a router doesn't have a name attribute
        """
        dir_path = Path(directory)

        for file_path in self.resolve_paths(dir_path):
            try:
                router = RouterParser.extract_router(file_path)
            except (ModuleNotFoundError, TypeError) as exc:
                loggers.routers.error(
                    "Error while trying to load router from %s: %s", file_path, exc
                )
                continue

            try:
                unique_name: str = router.name
            except AttributeError as e:
                msg = "The router has no name"
                raise AttributeError(msg) from e

            if unique_name in self.loaders:
                suffix = hex(id(router))
                unique_name = f"{router.name}_{suffix}"
                loggers.routers.warning(
                    "Duplicate router name: %s. Will rename to %s...",
                    router.name,
                    unique_name,
                )
                router.name = unique_name

            loader = RouterLoader(
                unique_name,
                file_path,
                self.dispatcher,
                router=router,
            )
            loader.load()
            self.loaders[unique_name] = loader
            loggers.routers.debug("Router loaded: %s", unique_name)

    async def start_watchdog(self, directory: StrOrPath) -> None:
        """Start file watching service.

        Monitors the specified directory for file changes and automatically
        reloads routers when their corresponding files are modified.

        :param directory: Directory to watch for changes
        :type directory: StrOrPath
        """
        loggers.routers.info("Router watchdog started for: %s", directory)
        base_directory = Path(directory).resolve()

        async for changes in awatch(directory, step=500):
            for event_type, changed_path in changes:
                path_object = Path(changed_path).resolve()

                try:
                    relative_path = Path("/") / path_object.relative_to(base_directory.parent)
                except ValueError:
                    relative_path = path_object

                current_loader: RouterLoader | None = None
                for loader in self.loaders.values():
                    if Path(loader.path).resolve() == path_object:
                        current_loader = loader
                        break

                if not current_loader:
                    loggers.routers.debug("File changed: %s. No routers found.", relative_path)
                    continue

                if event_type in (Change.modified, Change.added):
                    loggers.routers.debug("File changed: %s. Reloading...", relative_path)

                    try:
                        await current_loader.reload()
                    except Exception as exc:  # noqa: BLE001
                        loggers.routers.error(
                            "Router '%s' has an error '%s'. Skipping...",
                            current_loader.path,
                            exc,
                        )
                        continue

                elif event_type == Change.deleted:
                    loggers.routers.debug("File removed: %s. Unloading...", relative_path)
                    current_loader.unload()
                break
