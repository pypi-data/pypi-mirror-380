"""
Integration tests for the Rune library.

This test suite creates a temporary directory structure to validate
the core functionality of Rune in an isolated environment.
"""

import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path

# Add the source directory to the Python path for direct script execution
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from rune.loader import RuneLoader


class TestRuneIntegration(unittest.TestCase):
    """Validates end-to-end functionality of the Rune asset loader."""

    def setUp(self):
        """Set up a temporary directory with a mock project structure."""
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = Path.cwd()
        os.chdir(self.test_dir)

        # Create a mock asset structure
        self.resources_path = Path("resources")
        self.images_path = self.resources_path / "images"
        self.images_path.mkdir(parents=True)

        # Create a dummy file
        (self.images_path / "icon.png").touch()

        # Create a mock themes structure for discovery tests
        self.themes_path = self.resources_path / "themes"
        self.themes_path.mkdir()
        (self.themes_path / "dark.scss").touch()
        (self.themes_path / "light.scss").touch()
        (self.themes_path / "config.json").touch() # A non-theme file

    def tearDown(self):
        """Clean up the temporary directory and restore the CWD."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

        # Reset the singleton instance to ensure test isolation
        RuneLoader._instance = None

    def test_asset_discovery_and_access(self):
        """
        Tests if Rune can discover and provide access to a test asset.
        """
        # Instantiate a new loader to ensure it discovers the temp environment
        assets = RuneLoader()

        # 1. Test directory group access
        images_group = assets.images
        self.assertEqual(images_group, self.images_path.resolve())

        # 2. Test file access
        icon_path = assets.images.icon
        expected_path = (self.images_path / "icon.png").resolve()
        self.assertEqual(icon_path, expected_path)
        self.assertTrue(icon_path.exists())

        # 3. Test path joining with the '/' operator
        icon_path_join = assets.images / "icon.png"
        self.assertEqual(icon_path_join, expected_path)

    def test_discover_method(self):
        """Tests the ability to discover assets matching a pattern."""
        assets = RuneLoader()
        
        # Discover all .scss files
        discovered_themes = assets.themes.discover("*.scss")

        self.assertIsInstance(discovered_themes, dict)
        self.assertEqual(len(discovered_themes), 2)
        self.assertIn("dark", discovered_themes)
        self.assertIn("light", discovered_themes)
        self.assertNotIn("config", discovered_themes) # Ensure pattern is respected
        self.assertEqual(discovered_themes["dark"].name, "dark.scss")

    def test_get_method(self):
        """Tests programmatic asset retrieval using the get() method."""
        assets = RuneLoader()

        # Test successful retrieval
        icon_path = assets.images.get("icon")
        expected_path = (self.images_path / "icon.png").resolve()
        
        self.assertIsNotNone(icon_path)
        self.assertEqual(icon_path, expected_path)

        # Test failed retrieval
        missing_asset = assets.images.get("non_existent")
        self.assertIsNone(missing_asset)


if __name__ == "__main__":
    unittest.main()