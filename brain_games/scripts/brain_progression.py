from random import randint
from brain_games.game_func import welcome
from brain_games.game_func import get_name
from brain_games.game_func import check_answer
from brain_games.game_func import ask_question
from brain_games.game_func import correct
from brain_games.game_func import wrong_answer
from brain_games.game_func import try_again
from brain_games.game_func import a_progression


def main():
    welcome()
    name = get_name()

    print('What number is missing in the progression?')

    count = 3
    while count > 0:
        num1 = randint(1, 100)
        num2 = randint(1, 10)
        progression = a_progression(num1, num2)
        index = randint(0, 9)
        correct_answer = progression[index]
        progression[index] = '..'
        answer = ask_question(f'{" ".join([str(x) for x in progression])}')

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
