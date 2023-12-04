from random import randint


GAME_QUESTION = 'What number is missing in the progression?'


def game_question_and_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 10)
    progression = a_progression(num1, num2)
    index = randint(0, 9)
    correct_answer = progression[index]
    progression[index] = '..'
    question = f'{" ".join([str(x) for x in progression])}'
    return question, str(correct_answer)


def a_progression(a, d):
    res = []
    for i in range(10):
        res.append(a + i * d)
    return res
