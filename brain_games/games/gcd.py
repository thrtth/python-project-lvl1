from random import randint
from math import gcd


GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def game_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    return question, str(correct_answer)
