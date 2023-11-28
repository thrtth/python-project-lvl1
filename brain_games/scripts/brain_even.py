from random import randint
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

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 3
    while count > 0:
        num = randint(1, 100)
        answer = ask_question(num)
        correct_answer = 'no' if num % 2 else 'yes'
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
