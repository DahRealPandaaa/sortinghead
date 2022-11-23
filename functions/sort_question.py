from classes.question import question as question_class
from functions.firebase import get_questions
from classes.answer import answer
from functions.draw_question import draw_question
from init import speler
import random


def sort_question():
    speler.running = True
    questions = []
    # zet vragen in class en antwoorden in class
    for vragen in get_questions():
        answers = []
        for antwoord in vragen["Optie"]:
            answers.append(
                answer(antwoord["Answer"], antwoord["Score_FICT"], antwoord["Score_SE"], antwoord["Score_DE"],
                       antwoord["Score_IAT"], antwoord["Kenmerken"]))
        question = question_class(vragen["Vraag"], answers)
        questions.append(question)
    random.shuffle(questions)

    # teken vragen als er meer dan 1 vraag is
    if len(questions) > 0:
        draw_question(questions[0], questions, 0)
