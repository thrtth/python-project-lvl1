from random import randint


GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_question_and_answer():
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def is_prime(num):
    if num < 2:
        return False
    x = 2
    while num % x != 0:
        x += 1
    return x == num
