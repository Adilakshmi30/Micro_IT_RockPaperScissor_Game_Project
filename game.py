import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'quit']:
        choice = input("Invalid choice. Please enter rock, paper, scissors, or 'quit': ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        if user_choice == 'quit':
            break

        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie this round!")

        round_number += 1

    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < computer_score:
        print("Computer wins overall. Better luck next time!")
    else:
        print("It's an overall tie!")

play_game()

