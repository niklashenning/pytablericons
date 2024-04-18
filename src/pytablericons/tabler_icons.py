import io
import os
import contextlib
from PIL import Image
with contextlib.redirect_stdout(None):
    import pygame
from .outline_icon import OutlineIcon
from .filled_icon import FilledIcon


class TablerIcons:

    # Constants
    __DEFAULT_SVG_SIZE = 24

    @staticmethod
    def load(icon: OutlineIcon | FilledIcon, size: int = 24,
             color: str = "#FFF", stroke_width: float = 2.0) -> Image:
        """Load a specified Tabler icon into a Pillow Image
        with the option to provide a custom size, color, and stroke width

        :param icon: specified Tabler icon from the OutlineIcon or FilledIcon enum
        :param size: optional size of the icon
        :param color: optional color of the icon
        :param stroke_width: optional stroke-width of the icon
        :return: specified Tabler icon as Pillow Image
        """

        if type(icon) == OutlineIcon:
            color_property = 'stroke'
            svg_path = TablerIcons.__get_directory() + '/icons/outline/' + icon.value
        else:
            color_property = 'fill'
            svg_path = TablerIcons.__get_directory() + '/icons/filled/' + icon.value

        scale = size / TablerIcons.__DEFAULT_SVG_SIZE

        svg_string = open(svg_path, "rt").read()
        adjusted_svg_string = (svg_string.replace('width="' + str(TablerIcons.__DEFAULT_SVG_SIZE) + '"',
                                                  'width="' + str(size) + '"')
                               .replace('height="' + str(TablerIcons.__DEFAULT_SVG_SIZE) + '"',
                                        'height="' + str(size) + '"'
                                        ' transform="scale(' + str(scale) + ')"')
                               .replace('stroke-width="2"',
                                        'stroke-width="' + str(stroke_width) + '"')
                               .replace(color_property + '="currentColor"',
                                        color_property + '="' + color + '"'))

        svg_image = pygame.image.load(io.BytesIO(adjusted_svg_string.encode()))
        image_bytes = pygame.image.tobytes(svg_image, "RGBA")

        return Image.frombytes("RGBA", (size, size), image_bytes)

    @staticmethod
    def __get_directory():
        """Get the current directory path

        :return: directory path
        """

        return os.path.dirname(os.path.realpath(__file__))
