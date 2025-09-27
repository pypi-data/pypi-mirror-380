<h1 align="center">
    <img
        src="https://raw.githubusercontent.com/Yrrrrrf/manifold/main/resources/img/manifold.png"
        alt="Rune Icon"
        width="128" height="128"
        description="A rune that represents the concept of asset management."
    />
    <div align="center">rune</div>
</h1>

<div align="center">

<!-- todo: Update badges when the package is published on PyPI -->
<!-- [![PyPI version](https://img.shields.io/pypi/v/rune)](https://pypi.org/project/rune/) -->
[![GitHub: rune](https://img.shields.io/badge/GitHub-rune-181717?logo=github)](https://github.com/Yrrrrrf/manifold)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://choosealicense.com/licenses/mit/)
<!-- [![Downloads](https://pepy.tech/badge/rune)](https://pepy.tech/project/rune) -->

</div>

## Overview

A Python library for zero-configuration, OS-independent asset management. It automatically discovers and provides an intuitive API to access project files, eliminating the need for hardcoded relative paths or complex configuration.

Built on top of Python's native `pathlib`, rune eliminates boilerplate code related to path management. It adapts to your existing project structure, allowing you to focus on your application's logic instead of worrying about file locations.

## Key Features

- **Zero Configuration**: Works out-of-the-box by automatically detecting your project root and common asset directories (`assets/` or `resources/`).
- **Intuitive, Pythonic API**: Access your assets as if they were Python objects (`assets.images.player_icon`).
- **Cross-Platform Reliability**: Identical behavior across Windows, macOS, and Linux.
- **`pathlib` Integration**: Returns standard `pathlib.Path` objects for full compatibility with modern Python libraries.
- **Path-like Behavior**: Supports natural path joining with the `/` operator (`assets.fonts / "main.ttf"`).
- **Excellent Developer Experience**: Provides clear, helpful error messages with suggestions for typos.

## Installation

```bash
uv add rune
```

## Quick Start

Imagine you have the following project structure:

```
my_awesome_project/
├── resources/
│   ├── images/
│   │   ├── player.png
│   │   └── background.jpg
│   └── fonts/
│       └── main.ttf
└── src/
    └── main.py
```

In `main.py`, you can access your assets like this:


> **NOTE**: The asset paths are resolved relative to the project root, making it easy to manage assets without worrying about their physical locations.
> **NOTE**: The asset paths are case-insensitive, allowing for flexible access regardless of the original file naming.
> **NOTE**: The name `rune` is used as a namespace for now... I'm looking for a way to use it if possible, if not I'll just change the name of the pkg to something that fits better!
```python
from rune import assets

# Get the path to the player image
player_image_path = assets.images.player

# You can also use the / operator to join paths
main_font_path = assets.fonts / "main.ttf"

print(f"Player image: {player_image_path}")
print(f"Main font: {main_font_path}")
```

## API Behavior

`rune` dynamically maps your directory structure to a Python object.

-   **Directory Access**: `assets.images` maps to the first discoverable directory named `images/`.
-   **File Access**: `assets.images.player` maps to the file `images/player.png`. The file extension is optional and normalized.
-   **Path Joining**: `assets.images / "enemies/goblin.png"` works just like `pathlib`.
-   **Iteration**: `for file in assets.images: print(file)` allows you to iterate over contents.

## Usage Examples

See the [examples](./examples) directory for complete sample applications demonstrating various project layouts and use cases.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
