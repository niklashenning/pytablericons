# Python Tabler Icons

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://github.com/niklashenning/py-tabler-icons)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/niklashenning/py-tabler-icons)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/niklashenning/py-tabler-icons/blob/master/LICENSE)

Python cross-platform wrapper for the **[Tabler Icons](https://github.com/tabler/tabler-icons)** library - a set of 5237 free MIT-licensed high-quality SVG icons for you to use in your python projects

<p align="center">
  <a href="https://tabler-icons.io/"><strong>Browse at tabler-icons.io &rarr;</strong></a>
</p>

## Features
- 5237 free MIT-licensed high-quality SVG icons
- Supports custom icon size, color, and stroke width
- Supports IDE autocompletion for the icons
- Works cross-platform without any extra dependencies
- Works with `PyQt5`, `PyQt6`, `PySide2`, `PySide6`, `Tkinter`, etc.

## Installation
```python
pip install py-tabler-icons
```

## Usage
Import `TablerIcon` and call the `load()` method with the desired `OutlineIcon` or `FilledIcon`:
```python
from pytablericons import TablerIcon, OutlineIcon, FilledIcon

icon_rotate = TablerIcon.load(OutlineIcon.ROTATE)   # Outline icon
icon_hexagon = TablerIcon.load(FilledIcon.HEXAGON)  # Filled icon
```

> **NOTE:** <br>...

## Examples

- **Opening an icon with Pillow:**
```python
...
```

- **Using an icon with PyQt6:**
```python
...
```

## Customization
Setting a custom size, color, and stroke width:
```python
...
```

## Preview
### Outline version (<!--icons-count-outline-->4577<!--/icons-count-outline--> icons)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/preview/icons-outline-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/preview/icons-outline.png">
    <img src="https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/preview/icons-outline.png" alt="Tabler Icons preview" width="838">
  </picture>
</p>

### Filled version (<!--icons-count-filled-->660<!--/icons-count-filled--> icons)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/preview/icons-filled-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/preview/icons-filled.png">
    <img src="https://raw.githubusercontent.com/tabler/tabler-icons/master/.github/preview/icons-filled.png" alt="Tabler Icons preview" width="838">
  </picture>
</p>

## License
This software is licensed under the [MIT license](https://github.com/niklashenning/py-tabler-icons/blob/master/LICENSE).