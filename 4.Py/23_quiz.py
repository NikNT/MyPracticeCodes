def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key,_ in questions.items():
        print("-----------------")
        print(key)
        for option in options_list[question_number-1]:
            print(option)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        point = check_answer(questions.get(key), guess)
        correct_guesses += point
        question_number += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT!')
        return 1
    else:
        print('INCORRECT!')
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------------")
    print('RESULTS')
    print(f"Answers: ", end="")
    for que in questions:
        print(questions.get(que), end=" ")
    print()

    print("-------------------------------")
    print(f"GUESSES: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print(f"Your score is {str(score)}")


def play_again():
    user_input = input("Would you like to play again? (Y/N) ").upper()
    if user_input == "Y":
        return True
    else:
        print('BYE!')
        return False


questions = {
    "Who created Python?:" : "A",
    "What year was Python created?" : "B",
    "Python is tributed to which comedy group?" : "C",
    "Is the Earth round?:" : "A"
}

options_list = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2010"],
    ["A. The Marx Brothers", "B. Monty Python", "C. The Three Stooges", "D. The Beatles"],
    ["A. Yes", "B. No", "C. Flat", "D. Donut-shaped"]
]

new_game()
while play_again():
    new_game()