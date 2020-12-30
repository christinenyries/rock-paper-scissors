import random


def is_user_winner(user_choice, computer_choice):
    # r > s > p
    return (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "s" and computer_choice == "p")
        or (user_choice == "p" and computer_choice == "r")
    )


def play():
    choices = {"r": "rock", "p": "paper", "s": "scissors"}

    user_choice = None
    while user_choice not in choices.keys():
        user_choice = input("Enter (r) for rock, (p) for paper, or (s) for scissors: ")

    computer_choice = random.choice(list(choices.keys()))

    print(f"You chose {choices[user_choice]}")
    print(f"The computer chose {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif is_user_winner(user_choice, computer_choice):
        print("You won!")
    else:
        print("You lost. Try again")


if __name__ == "__main__":
    play()