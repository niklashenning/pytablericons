# pytablericons

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://github.com/niklashenning/pytablericons)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/niklashenning/pytablericons)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/niklashenning/pytablericons/blob/master/LICENSE)

Python wrapper for the **[Tabler Icons](https://github.com/tabler/tabler-icons)** library - a set of 5237 free MIT-licensed high-quality SVG icons for you to use in your python projects

<p align="center">
  <a href="https://tabler-icons.io/"><strong>Browse at tabler-icons.io &rarr;</strong></a>
</p>

<p align="center">
  <img src="https://github.com/niklashenning/py-tabler-icons/assets/58544929/9b31b411-04a0-452e-9aaa-ce9b3d8a2b45" alt="Tabler Icons" width="775">
</p>

## Features
- 5237 free MIT-licensed high-quality SVG icons
- Supports custom icon size, color, and stroke width
- Supports IDE autocompletion
- Works cross-platform without any extra dependencies
- Easy to use with `Pillow`, `PyQt5`, `PyQt6`, `PySide2`, `PySide6`, `Tkinter`, etc.

## Installation
```python
pip install pytablericons
```

## Usage
Import `TablerIcons` and call the `load()` method with the desired `OutlineIcon` or `FilledIcon`:
```python
from pytablericons import TablerIcons, OutlineIcon, FilledIcon

icon_rotate = TablerIcons.load(OutlineIcon.ROTATE)      # Outline icon
icon_check = TablerIcons.load(FilledIcon.CIRCLE_CHECK)  # Filled icon
```

> **NOTE:** <br>...

## Customization
Setting a custom size, color, and stroke width:
```python
...
```

> **NOTE:** <br>...

## Examples

- **Using an icon with Pillow:**
```python
from pytablericons import TablerIcons, FilledIcon

icon = TablerIcons.load(FilledIcon.CIRCLE_CHECK)  # Load icon
icon.show()  # Show icon
print(icon.size)  # Print icon size
```

- **Using an icon with PyQt6:**
```python
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton
from pytablericons import TablerIcons, OutlineIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        
        # Load icon
        icon_rotate = TablerIcons.load(OutlineIcon.ROTATE, color='#000')
        
        # Create button with icon
        self.button = QPushButton(self)
        self.button.setText('Rotate')
        self.button.setIcon(QIcon(icon_rotate.toqpixmap()))
```

More in-depth examples can be found in the [examples](examples) folder.

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
This software is licensed under the [MIT license](https://github.com/niklashenning/pytablericons/blob/master/LICENSE).