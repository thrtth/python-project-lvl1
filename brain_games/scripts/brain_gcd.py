from random import randint
from math import gcd
from brain_games.game_func import welcome
from brain_games.game_func import get_name
from brain_games.game_func import check_answer
from brain_games.game_func import ask_question
from brain_games.game_func import correct
from brain_games.game_func import wrong_answer
from brain_games.game_func import try_again


def main():
    welcome()
    name = get_name()

    print('Find the greatest common divisor of given numbers.')

    count = 3
    while count > 0:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        answer = ask_question(f'{num1} {num2}')
        correct_answer = gcd(num1, num2)

        if check_answer(answer, correct_answer):
            correct()
        else:
            wrong_answer(answer, correct_answer)
            try_again(name)
            exit()
        count -= 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
