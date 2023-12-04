from random import randint


GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_question_and_answer():
    num = randint(1, 100)
    question = num
    correct_answer = 'no' if num % 2 else 'yes'
    return question, correct_answer
