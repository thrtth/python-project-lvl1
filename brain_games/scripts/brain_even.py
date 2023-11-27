import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 3
    while count > 0:
        num = randint(1, 100)

        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'no' if num % 2 else 'yes'

        if answer == correct_answer:
            print('Correct!')
            count -= 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            exit()

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
