from init import canvas1, cam, screen_height, speler
from PIL import ImageTk, Image as Image_pil
from tkinter import *
from functions.rescale import rescale
from functions.detectface import detect_face


def draw():
    if speler.running:
        # Webcam
        label = Label(canvas1)

        # open foto sorting hat en resize
        image_sortinghead = Image_pil.open("img/sorting_hat.png")
        image_sortinghead = image_sortinghead.resize((195, 145), Image_pil.ANTIALIAS)

        # get frames from webcam
        image_webcam, gray_image = cam.get_frame()

        # detect face
        detect_face(gray_image)
        image_webcam = image_webcam.convert("RGBA")

        # Zet hoed op webcam
        image_webcam.paste(image_sortinghead, (cam.get_face()), image_sortinghead)

        image_webcam = rescale(image_webcam)

        # resize image

        # zet image naar formaat wat tkinter kan gebruiken
        imgtk = ImageTk.PhotoImage(image=image_webcam)

        # zet image op canvas
        label.place(y=screen_height / 2 - 50, x=25)
        label.imgtk = imgtk
        label.configure(image=imgtk, highlightbackground="#5e4630", highlightthickness=5, borderwidth=0)

        # na 1/60 van een seconde runt dit opnieuw en 15 ms word de frame gedelete
        label.after(int(1000 / 60), draw)
        canvas1.after(int(1000 / 60) + 15, lambda: label.destroy())
