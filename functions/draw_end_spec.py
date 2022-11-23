from init import se, fict, iat, de, allspec, screen_width, screen_height
from tkinter import *
import tkinter.font as tkFont

def draw_end_spec(canvas, winner):
    if len(winner) == 1:
        if winner[0] == "Software Engineer":
            canvas.create_image(0, 0, image=se, anchor="nw")
        elif winner[0] == "Forensisch ICT":
            canvas.create_image(0, 0, image=fict, anchor="nw")
        elif winner[0] == "Interactie-Technologie":
            canvas.create_image(0, 0, image=iat, anchor="nw")
        elif winner[0] == "Data Engineer":
            canvas.create_image(0, 0, image=de, anchor="nw")
        canvas.pack(fill="both", expand=True)
    else:
        canvas.create_image(0, 0, image=allspec, anchor="nw")
        perpetua = tkFont.Font(family="Perpetua Titling MT", size=32)
        label_kenmerk1 = Label(canvas,
                               text=f"Jouw specialisatie is..."
                                    f"\n\n{', '.join(winner)} "
                                    f"",
                               font=perpetua,
                               fg="white",
                               bg="black",
                               wraplength=screen_width / 10 * 8,
                               height=3)
        label_kenmerk1.place(x=screen_width / 2, y=5, anchor="n")
        canvas.pack(fill="both", expand=True)
