from random import randint
from random import choice


GAME_QUESTION = 'What is the result of the expression?'


def game_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operation = choice('-+*')
    question = f'{num1} {operation} {num2}'
    correct_answer = ''
    match operation:
        case '-':
            correct_answer = num1 - num2
        case '+':
            correct_answer = num1 + num2
        case '*':
            correct_answer = num1 * num2

    return question, str(correct_answer)
