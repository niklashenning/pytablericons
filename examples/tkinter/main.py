from PIL import ImageTk
from tkinter import Tk, Canvas, Button
from tkinter.constants import *
from src.pytablericons import TablerIcons, OutlineIcon, FilledIcon


# Initialize window
root = Tk()
root.geometry('370x170')
root.title('pytablericons')

# Load icon and convert to ImageTk
icon_rotate = TablerIcons.load(OutlineIcon.ROTATE, size=16,
                               color='#000', stroke_width=3.0)
icon_rotate_tk_image = ImageTk.PhotoImage(icon_rotate)

# Create button with icon
button = Button(root, text='Rotate', image=icon_rotate_tk_image, compound=LEFT)
button.pack(pady=20)

# Load icon and convert to ImageTk
CANVAS_ICON_SIZE = 70
icon_check = TablerIcons.load(FilledIcon.CIRCLE_CHECK,
                              size=CANVAS_ICON_SIZE, color='#4444e5')
icon_check_tk_image = ImageTk.PhotoImage(icon_check)

# Create canvas and display icon
canvas = Canvas(root, width=CANVAS_ICON_SIZE, height=CANVAS_ICON_SIZE)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=icon_check_tk_image)

# Run event loop
root.mainloop()
