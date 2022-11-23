from init import canvas1, speler, win, screen_width, screen_height
from tkinter import *
from functions.end_data import end_data
from functions.close_win import close_win
from functions.draw_end_spec import draw_end_spec
import tkinter.font as tkfont


def end_screen():
    speler.running = False
    # haal winner en kenmerken op
    winner, kenmerken_string = end_data()
    # hide main screen
    canvas1.pack_forget()

    # haal eindscherm images op

    # maak eindscherm
    canvas_end = Canvas(win, width=screen_width, height=screen_height)
    # kijk of er 1 winnaar is
    draw_end_spec(canvas_end, winner)
    perpetuanormal = tkfont.Font(family="Perpetua", size=20, weight="bold", slant="italic")

    # maak labels voor kenmerken
    label_kenmerk1 = Label(canvas_end,
                           text=f"Je bent ingedeeld bij deze specialisastie omdat je door de vragen te beantwoorden "
                                f"je interesse liggen bij de volgende kenmerken: \n{kenmerken_string} "
                                f"",
                           font=perpetuanormal,
                           fg="#5e4630",
                           bg="#BA8C63",
                           borderwidth=5,
                           relief="raised",
                           wraplength=screen_width / 10 * 8 - 50,
                           height=5)
    label_kenmerk1.place(x=screen_width / 2, y=screen_height - 15, anchor="s")
    # Button maken met nee en ja waarbij nee het spel afsluit en ja de vragen start
    from functions.start import start
    button_end = Button(canvas_end)
    button_end.configure(text="Quit!",
                         fg="#5e4630",
                         bg="#BA8C63",
                         font=perpetuanormal,
                         height=2,
                         width=15,
                         borderwidth=5,
                         relief="raised",
                         command=lambda: close_win())
    button_end.place(x=screen_width / 2 - 25, y=(screen_height / 2 + 175), anchor="e")

    button = Button(canvas_end)
    button.configure(text="Restart!",
                     fg="#5e4630",
                     bg="#BA8C63",
                     font=perpetuanormal,
                     height=2,
                     width=15,
                     borderwidth=5,
                     relief="raised",
                     command=lambda: (
                         speler.reset(),
                         canvas_end.destroy(),
                         start()
                     ))
    button.place(x=screen_width / 2 + 50, y=(screen_height / 2 + 175), anchor="w")
