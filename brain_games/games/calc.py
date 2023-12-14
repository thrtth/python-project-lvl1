from random import randint
from random import choice
from operator import add, mul, sub


GAME_QUESTION = 'What is the result of the expression?'


def game_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    func, operation = choice([(add, '+'), (sub, '-'), (mul, '*')])
    question = f'{num1} {operation} {num2}'
    correct_answer = func(num1, num2)
    return question, str(correct_answer)
