from functions.draw import draw
from functions.sort_question import sort_question
from tkinter import *
from init import win, screen_width, screen_height, canvas1, bg_start
from functions.close_win import close_win
import tkinter.font as tkfont


def start():
    # canvas1 hiden
    canvas1.pack_forget()
    perpetua = tkfont.Font(family="Perpetua Titling MT", size=22)
    perpetuanormal = tkfont.Font(family="Perpetua", size=20, weight="bold", slant="italic")

    # canvas2 maken voor start scherm
    canvas_start = Canvas(win, width=screen_width,
                          height=screen_height)
    canvas_start.create_image(0, 0, image=bg_start,
                              anchor="nw")
    canvas_start.pack(fill="both", expand=True)

    # Text op start schem maken
    text_label = Label(canvas_start,
                       text="Ben jij bereid om je lot te ontdekken?",
                       font=perpetua,
                       height="2",
                       fg="#5e4630",
                       bg="#BA8C63",
                       borderwidth=5,
                       relief="raised",
                       width=int(((screen_width / 10 * 4) / screen_width) * 100),
                       wraplength=screen_width / 5 * 2
                       )
    text_label.place(x=screen_width / 2, y=screen_height / 2 + 175, anchor="center")

    # Button maken met nee en ja waarbij nee het spel afsluit en ja de vragen start
    button2 = Button(canvas_start)
    button2.configure(text="Nee, dat wil ik niet!",
                      fg="#5e4630",
                      bg="#BA8C63",
                      font=perpetuanormal,
                      height=3,
                      width=25,
                      borderwidth=5,
                      relief="raised",
                      command=lambda: close_win())
    button2.place(x=screen_width / 2 - 25, y=(screen_height / 2 + 300), anchor="e")

    button = Button(canvas_start)
    button.configure(text="Ja, ik wil mijn lot ontdekken!",
                     fg="#5e4630",
                     bg="#BA8C63",
                     font=perpetuanormal,
                     height=3,
                     width=25,
                     borderwidth = 5,
                     relief="raised",
                     command=lambda: (
                         canvas_start.destroy(),
                         canvas1.pack(fill="both", expand=True),
                         sort_question(),
                         draw(),
                     ))
    button.place(x=screen_width / 2 + 25, y=(screen_height / 2 + 300), anchor="w")
