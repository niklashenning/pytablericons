from src.pytablericons import TablerIcons, OutlineIcon, FilledIcon


# Outline icon
icon_rotate = TablerIcons.load(OutlineIcon.ROTATE)
icon_rotate.show()
print(icon_rotate.size)

# Filled icon with custom size and color
icon_check = TablerIcons.load(FilledIcon.CIRCLE_CHECK, size=100, color='red')
icon_check.show()
print(icon_check.size)
