import prompt


NUMBER_OF_ROUNDS = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_QUESTION)

    count = 1
    while count <= NUMBER_OF_ROUNDS:
        question, correct_answer = game.game_question_and_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            exit()
        count += 1
    print(f'Congratulations, {name}!')
