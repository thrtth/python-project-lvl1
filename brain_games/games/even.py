from random import randint


GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question_and_answer():
    question = randint(1, 100)
    correct_answer = 'no' if question % 2 else 'yes'
    return question, correct_answer
