from random import randint
from brain_games.game_func import welcome
from brain_games.game_func import get_name
from brain_games.game_func import check_answer
from brain_games.game_func import ask_question
from brain_games.game_func import correct
from brain_games.game_func import wrong_answer
from brain_games.game_func import is_prime


def main():
    welcome()
    name = get_name()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 3
    while count > 0:
        num = randint(1, 100)
        answer = ask_question(num)
        correct_answer = 'yes' if is_prime(num) else 'no'
        if check_answer(answer, correct_answer):
            correct()
        else:
            wrong_answer(answer, correct_answer)
            exit()
        count -= 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
