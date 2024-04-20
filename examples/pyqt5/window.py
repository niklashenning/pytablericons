from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from src.pytablericons import TablerIcons, OutlineIcon, FilledIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # Window settings
        self.resize(360, 145)
        self.setWindowTitle('pytablericons')

        # Load icon
        BUTTON_ICON_SIZE = 18
        icon_rotate = TablerIcons.load(OutlineIcon.ROTATE, size=BUTTON_ICON_SIZE,
                                       color='#000', stroke_width=2.5)

        # Convert icon to QImage
        # (A workaround like this is necessary for PyQt5 if you're on Pillow version >= 10.0.0
        #  since Qt 5 has reached end-of-life and support has been dropped in version 10.0.0.
        #  If you're using an older Pillow version, you can use the same code as with PyQt6)
        # See https://pillow.readthedocs.io/en/stable/deprecations.html#pyqt5-and-pyside2
        icon_rotate_q_image = QImage(icon_rotate.tobytes('raw', 'RGBA'), icon_rotate.width,
                                     icon_rotate.height, QImage.Format.Format_RGBA8888)

        # Create button with icon
        self.button = QPushButton(self)
        self.button.setText('Rotate')
        self.button.setIcon(QIcon(QPixmap.fromImage(icon_rotate_q_image)))
        self.button.setIconSize(QSize(BUTTON_ICON_SIZE, BUTTON_ICON_SIZE))

        # Load icon
        PIXMAP_ICON_SIZE = 70
        icon_check = TablerIcons.load(FilledIcon.CIRCLE_CHECK,
                                      size=PIXMAP_ICON_SIZE, color='#4444e5')

        # Convert icon to QImage (same reason as above)
        icon_check_q_image = QImage(icon_check.tobytes('raw', 'RGBA'), icon_check.width,
                                    icon_check.height, QImage.Format.Format_RGBA8888)

        # Create label and display pixmap
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(icon_check_q_image))
        self.label.setFixedSize(PIXMAP_ICON_SIZE, PIXMAP_ICON_SIZE)

        # Vertical layout
        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vbox_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox_layout.setSpacing(20)
        self.vbox_layout.setContentsMargins(20, 20, 20, 20)

        # Set layout
        central_widget = QWidget()
        central_widget.setLayout(self.vbox_layout)
        self.setCentralWidget(central_widget)
