# playing with 2 players and 1 computer

import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player1 = None
    player2 = None
    computer = random.choice(options)

    # Get choices from both players
    while player1 not in options:
        player1 = input("Player 1, enter a choice (rock, paper, scissors): ").lower()
    
    while player2 not in options:
        player2 = input("Player 2, enter a choice (rock, paper, scissors): ").lower()

    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")
    print(f"Computer: {computer}")

    # Determine the winner against the computer
    def determine_winner(choice, computer_choice):
        if choice == computer_choice:
            return "Tie"
        elif (choice == "rock" and computer_choice == "scissors") or \
             (choice == "paper" and computer_choice == "rock") or \
             (choice == "scissors" and computer_choice == "paper"):
            return "Win"
        else:
            return "Lose"

    result1 = determine_winner(player1, computer)
    result2 = determine_winner(player2, computer)

    # Determine the outcome for both players
    def print_result(player, result):
        if result == "Tie":
            return f"{player} ties with the Computer!"
        elif result == "Win":
            return f"{player} wins against the Computer!"
        else:
            return f"{player} loses to the Computer!"

    print(print_result("Player 1", result1))
    print(print_result("Player 2", result2))

    if input("Play again? (yes/no): ").lower() != "yes":
        running = False

print("Thanks for Playing!")
