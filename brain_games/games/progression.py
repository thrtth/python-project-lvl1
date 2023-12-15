from random import randint


GAME_QUESTION = 'What number is missing in the progression?'
AMOUNT_OF_ELEMENTS = 10


def game_question_and_answer():
    start = randint(1, 100)
    step = randint(1, 10)
    end = start + step * AMOUNT_OF_ELEMENTS
    progression = list(range(start, end, step))
    index = randint(0, 9)
    correct_answer = progression[index]
    progression[index] = '..'
    question = " ".join(map(str, progression))
    return question, str(correct_answer)
