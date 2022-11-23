from tkinter import *
from classes.webcam import webcam
from classes.player import player
from PIL import Image as Image_pil, ImageTk

win = Tk()

win.attributes('-fullscreen', True)
win.title("Sorting Head")
win.attributes('-transparentcolor', '#d4d4e2')
win.geometry("1920x1080")

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
bg = Image_pil.open('img/bg1.png')
bg = bg.resize((screen_width, screen_height), Image_pil.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(bg)

bg_start = Image_pil.open('img/bg2.png')
bg_start = bg_start.resize((screen_width, screen_height), Image_pil.Resampling.LANCZOS)
bg_start = ImageTk.PhotoImage(bg_start)

canvas1 = Canvas(win, width=screen_width,
                 height=screen_height)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")

label = Label(win)
cam = webcam()
speler = player()

# open image
se = Image_pil.open('img/se.png')
# resize image
se = se.resize((screen_width, screen_height))
# convert image to tkinter format
se = ImageTk.PhotoImage(se)

de = Image_pil.open('img/de.png')
de = de.resize((screen_width, screen_height))
de = ImageTk.PhotoImage(de)

iat = Image_pil.open('img/iat.png')
iat = iat.resize((screen_width, screen_height))
iat = ImageTk.PhotoImage(iat)

fict = Image_pil.open('img/fict.png')
fict = fict.resize((screen_width, screen_height))
fict = ImageTk.PhotoImage(fict)

allspec = Image_pil.open('img/all.png')
allspec = allspec.resize((screen_width, screen_height))
allspec = ImageTk.PhotoImage(allspec)
