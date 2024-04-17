import io
import os
import pygame
from PIL import Image
from .outline_icon import OutlineIcon
from .filled_icon import FilledIcon


class TablerIcon:

    # Constants
    __SVG_SIZE = 24

    @staticmethod
    def load(icon: OutlineIcon | FilledIcon, size: int = __SVG_SIZE,
             color: str = "#FFF", stroke_width: float = 2.0) -> Image:
        """...

        :param icon:
        :param size:
        :param color:
        :param stroke_width:
        :return:
        """

        if type(icon) == OutlineIcon:
            color_property = 'stroke'
            svg_path = TablerIcon.__get_directory() + '/icons/outline/' + icon.value
        else:
            color_property = 'fill'
            svg_path = TablerIcon.__get_directory() + '/icons/filled/' + icon.value

        scale = size / TablerIcon.__SVG_SIZE

        svg_string = open(svg_path, "rt").read()
        resized_svg_string = (svg_string.replace('width="' + str(TablerIcon.__SVG_SIZE) + '"',
                                                 'width="' + str(size) + '"')
                              .replace('height="' + str(TablerIcon.__SVG_SIZE) + '"',
                                       'height="' + str(size) + '"'
                                       ' transform="scale(' + str(scale) + ')"')
                              .replace('stroke-width="2"',
                                       'stroke-width="' + str(stroke_width) + '"')
                              .replace(color_property + '="currentColor"',
                                       color_property + '="' + color + '"'))

        svg_image = pygame.image.load(io.BytesIO(resized_svg_string.encode()))
        image_bytes = pygame.image.tobytes(svg_image, "RGBA")
        image = Image.frombytes("RGBA", (size, size), image_bytes)

        return image

    @staticmethod
    def __get_directory():
        """Get the current directory path

        :return: directory path
        """

        return os.path.dirname(os.path.realpath(__file__))
