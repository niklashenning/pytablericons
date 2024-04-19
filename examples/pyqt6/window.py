from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
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

        # Create button with icon
        self.button = QPushButton(self)
        self.button.setText('Rotate')
        self.button.setIcon(QIcon(icon_rotate.toqpixmap()))
        self.button.setIconSize(QSize(BUTTON_ICON_SIZE, BUTTON_ICON_SIZE))

        # Load icon
        PIXMAP_ICON_SIZE = 70
        icon_check = TablerIcons.load(FilledIcon.CIRCLE_CHECK,
                                      size=PIXMAP_ICON_SIZE, color='#4444e5')

        # Create label and display pixmap
        self.label = QLabel(self)
        self.label.setPixmap(icon_check.toqpixmap())
        self.label.setFixedSize(PIXMAP_ICON_SIZE, PIXMAP_ICON_SIZE)

        # Vertical layout
        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.vbox_layout.setSpacing(20)
        self.vbox_layout.setContentsMargins(20, 20, 20, 20)

        # Set layout
        central_widget = QWidget()
        central_widget.setLayout(self.vbox_layout)
        self.setCentralWidget(central_widget)
