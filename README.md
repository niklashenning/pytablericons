# pytablericons

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/pytablericons)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/niklashenning/pytablericons)
[![Build](https://img.shields.io/badge/build-passing-neon)](https://github.com/niklashenning/pytablericons)
[![Coverage](https://img.shields.io/badge/coverage-100%25-green)](https://github.com/niklashenning/pytablericons)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/niklashenning/pytablericons/blob/master/LICENSE)

Python wrapper for the **[Tabler Icons](https://github.com/tabler/tabler-icons)** library - a set of 5237 free MIT-licensed high-quality SVG icons for you to use in your python projects

<p align="center">
  <a href="https://tabler-icons.io/"><strong>Browse at tabler-icons.io &rarr;</strong></a>
</p>

<p align="center">
  <img src="https://github.com/niklashenning/pytablericons/assets/58544929/e13fb020-4d5f-4e28-bd5f-0d5659bd6582" alt="pytablericons" width="1009">
</p>

## Features
- 5237 free MIT-licensed high-quality SVG icons
- Load icons into Pillow Image with custom size, color, and stroke width
- Supports IDE autocompletion
- Works cross-platform without any extra dependencies
- Easy to use with `Pillow`, `PyQt5`, `PyQt6`, `PySide2`, `PySide6`, `Tkinter`, etc.

## Installation
```python
pip install pytablericons
```

## Usage
Import `TablerIcons` and call the static `load()` method with the desired `OutlineIcon` or `FilledIcon`:
```python
from pytablericons import TablerIcons, OutlineIcon, FilledIcon

icon_rotate = TablerIcons.load(OutlineIcon.ROTATE)      # Outline icon
icon_check = TablerIcons.load(FilledIcon.CIRCLE_CHECK)  # Filled icon
```

> **NOTE:** <br>The icon names are the same as on the tabler-icons.io site, except every letter is uppercase and hyphens are replaced with underscores.<br>Examples: `rotate` &rarr; `ROTATE`, `arrow-down-right` &rarr; `ARROW_DOWN_RIGHT`

## Customization
Setting a custom size, color, and stroke width:
```python
# Width and height 100px (default: 24)
icon_custom_size = TablerIcons.load(OutlineIcon.ROTATE, size=100)

# Color red (default: '#FFF')
icon_custom_color = TablerIcons.load(OutlineIcon.ROTATE,  color='#ff0000')

# Stroke width 1.5 (default: 2.0)
icon_custom_stroke_width = TablerIcons.load(OutlineIcon.ROTATE, stroke_width=1.5)

# Combining everything
icon_custom = TablerIcons.load(OutlineIcon.ROTATE, size=100, color='#ff0000', stroke_width=1.5)
```

> **NOTE:** <br>The color can either be a **hex color** or one of very limited **color names**. <br>Examples: `'#ec3440'`, `'#581790'`, `'red'`, `'green'`, `'blue'`

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

- **Using an icon with Tkinter:**
```python
from PIL import ImageTk
from tkinter import Tk, Button
from tkinter.constants import *
from pytablericons import TablerIcons, OutlineIcon


# Create window
root = Tk()

# Load icon and convert to ImageTk
icon_rotate = TablerIcons.load(OutlineIcon.ROTATE, size=16, color='#000', stroke_width=3.0)
icon_rotate_tk_image = ImageTk.PhotoImage(icon_rotate)

# Create button with icon
button = Button(root, text='Rotate', image=icon_rotate_tk_image, compound=LEFT)
button.pack(padx=50, pady=25)

# Run event loop
root.mainloop()
```

More in-depth examples can be found in the [examples](https://github.com/niklashenning/pytablericons/blob/master/examples) folder.

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

## Tests
Installing the required test dependencies [pytest](https://github.com/pytest-dev/pytest) and [coveragepy](https://github.com/nedbat/coveragepy):
```
pip install pytest coverage
```

To run the tests with coverage, clone this repository, go into the main directory and run:
```
coverage run -m pytest
coverage report --ignore-errors -m
```

## License
This software is licensed under the [MIT license](https://github.com/niklashenning/pytablericons/blob/master/LICENSE).