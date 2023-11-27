import prompt


def welcome():
    print('Welcome to the Brain Games!')


def get_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer


def check_answer(answer, correct_answer):
    if answer == str(correct_answer):
        return True
    else:
        return False


def correct():
    print('Correct!')


def wrong_answer(answer, correct_answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")


def try_again(name):
    print(f"Let's try again, {name}!")