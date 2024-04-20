from src.pytablericons import TablerIcons, OutlineIcon, FilledIcon


def test_load_outline_icon():
    """Test loading an outline icon"""

    icon = TablerIcons.load(OutlineIcon.USER)

    assert icon.width == 24
    assert icon.height == 24
    assert icon.mode == "RGBA"
    assert (0, 0, 0, 0) == icon.getpixel((0, 0))  # Transparent pixel
    assert (255, 255, 255, 255) == icon.getpixel((10, 10))  # White pixel


def test_load_filled_icon():
    """Test loading a filled icon"""

    icon = TablerIcons.load(FilledIcon.USER)

    assert icon.width == 24
    assert icon.height == 24
    assert icon.mode == "RGBA"
    assert (0, 0, 0, 0) == icon.getpixel((0, 0))  # Transparent pixel
    assert (255, 255, 255, 255) == icon.getpixel((10, 10))  # White pixel


def test_load_outline_icon_custom():
    """Test loading an outline icon with custom size and color"""

    icon = TablerIcons.load(OutlineIcon.USER, size=200, color="#ff0000")

    assert icon.width == 200
    assert icon.height == 200
    assert icon.mode == "RGBA"
    assert (0, 0, 0, 0) == icon.getpixel((0, 0))  # Transparent pixel
    assert (255, 0, 0, 255) == icon.getpixel((150, 150))  # Red pixel


def test_load_filled_icon_custom():
    """Test loading a filled icon with custom size and color"""

    icon = TablerIcons.load(FilledIcon.USER, size=200, color="#ff0000")

    assert icon.width == 200
    assert icon.height == 200
    assert icon.mode == "RGBA"
    assert (0, 0, 0, 0) == icon.getpixel((0, 0))  # Transparent pixel
    assert (255, 0, 0, 255) == icon.getpixel((150, 150))  # Red pixel
