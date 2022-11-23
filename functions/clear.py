from init import canvas1
from functions.draw import draw


def clear():
    for widget in canvas1.winfo_children():
        widget.destroy()

    draw()
