"""
Handles the dynamic, attribute-based access to asset paths.
"""

from __future__ import annotations

from pathlib import Path
from typing import Self

from rune.exceptions import AssetNotFoundError


class DynamicAssetGroup(Path):
    """
    Represents a directory or file in the asset hierarchy, enabling dynamic
    attribute access while behaving exactly like a `pathlib.Path`.

    This class is the core of Rune's intuitive API, translating attribute
    access like `assets.images.player` into file system paths.
    """

    def __new__(cls, *args) -> Self:
        """
        Constructs the DynamicAssetGroup as a Path-like object.

        This method intercepts the arguments to prevent recursion when pathlib
        internal methods (like joinpath) attempt to create a new instance of
        this subclass.
        """
        # Convert any DynamicAssetGroup instances in args to strings to break recursion
        str_args = [str(arg) if isinstance(arg, DynamicAssetGroup) else arg for arg in args]
        return super().__new__(cls, *str_args)

    def discover(self, pattern: str = "*") -> dict[str, Path]:
        """
        Discovers all files within this directory matching a glob pattern.

        Args:
            pattern: A glob pattern (e.g., "*.scss", "icon_*.*").

        Returns:
            A dictionary mapping the asset's stem (filename without extension)
            to its full `pathlib.Path` object.
        """
        if not self.is_dir():
            return {}

        return {
            item.stem: item
            for item in self.glob(pattern)
            if item.is_file()
        }

    def get(self, name: str) -> Self | None:
        """
        Programmatically retrieves a file or directory by its name (stem).

        This provides a functional equivalent to attribute access (e.g., `assets.images.get('player')`
        is the same as `assets.images.player`).

        Args:
            name: The stem name of the asset to find (e.g., "player" for "player.png").

        Returns:
            A new `DynamicAssetGroup` instance representing the path, or `None` if not found.
        """
        # First, check for a directory with the exact name
        target_path = self / name
        if target_path.is_dir():
            return self.__class__(target_path)

        # If not a directory, search for a file with a matching name (extension-insensitive)
        if self.is_dir():
            for item in self.iterdir():
                if item.is_file() and item.stem.lower() == name.lower():
                    return self.__class__(item)

        return None

    def __getattr__(self, name: str) -> Self:
        """
        Dynamically access a file or subdirectory within this asset group.

        Args:
            name: The name of the file or directory to access.

        Returns:
            A new `DynamicAssetGroup` instance representing the target path.
        """
        # Do not interfere with internal attributes of the Path class.
        if name.startswith("_"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )
        # First, check for a directory with the exact name
        target_path = self / name
        if target_path.is_dir():
            return self.__class__(target_path)

        # If not a directory, search for a file with a matching name (extension-insensitive)
        # This is what allows for `assets.images.player` instead of `assets.images.player_png`
        if self.is_dir():
            for item in self.iterdir():
                if item.is_file() and item.stem.lower() == name.lower():
                    return self.__class__(item)

        # Fallback for cases where the user might include the extension
        if target_path.exists():
            return self.__class__(target_path)

        # todo: Add typo suggestions and proper error handling with AssetNotFoundError
        raise AssetNotFoundError(f"Asset '{name}' not found in '{self}'")

    def __repr__(self) -> str:
        return f"<DynamicAssetGroup path='{super().__repr__()}'>"
