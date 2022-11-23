from init import canvas1, speler, screen_width, screen_height
from tkinter import *
import random
from functions.clear import clear
from functions.endscreen import end_screen
from classes.question import question
import tkinter.font as tkfont


def draw_question(question_class: classmethod(question), questions: list, index: int):
    if index < len(questions) - 1:
        perpetua = tkfont.Font(family="Perpetua Titling MT", size=22)
        label_vraag = Label(canvas1,
                            text=question_class.question,
                            font=perpetua,
                            fg="#5e4630",
                            bg="#BA8C63",
                            width=int(((screen_width / 10 * 3) / screen_width) * 100 +2),
                            height=6,
                            wraplength=screen_width / 5 * 1.9,
                            borderwidth=5,
                            relief="raised"
                            )
        label_vraag.place(x=screen_width / 10 * 6, y=150, anchor="center")
        random.shuffle(question_class.answers)

        for antwoord_count, antwoord in enumerate(question_class.answers):
            # maak antwoord knop
            button = Button(canvas1)
            perpetuanormal = tkfont.Font(family="Perpetua", size=20, weight="bold", slant="italic")
            button.configure(text=antwoord.answer,
                             fg="#5e4630",
                             bg="#BA8C63",
                             font=perpetuanormal,
                             height=2,
                             width=int(((screen_width / 10 * 6) / screen_width) * 100 + 8),
                             wraplength=screen_width / 10 * 6 - 75,
                             borderwidth=5,
                             relief="raised",
                             command=lambda antwoord=antwoord: (
                                 speler.set_score(antwoord.se, antwoord.fict, antwoord.iat, antwoord.de),
                                 speler.kenmerken.update(antwoord.kenmerken),
                                 clear(),
                                 draw_question(questions[index + 1], questions, index + 1)
                             ))
            button.place(x=screen_width / 10 * 6, y=(screen_height / 2 - 50 + (antwoord_count * 110)), anchor="center")
    else:
        end_screen()


