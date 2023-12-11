from random import randint


GAME_QUESTION = 'What number is missing in the progression?'
AMOUNT_OF_ELEMENTS = 10


def game_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 10)
    progression = list(range(num1, (num1 + num2 * AMOUNT_OF_ELEMENTS), num2))
    index = randint(0, 9)
    correct_answer = progression[index]
    progression[index] = '..'
    question = f'{" ".join([str(x) for x in progression])}'
    return question, str(correct_answer)
