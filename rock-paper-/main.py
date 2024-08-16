# Player playing with two computers 

import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer1 = random.choice(options)
    computer2 = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer 1: {computer1}")
    print(f"Computer 2: {computer2}")

    # Determine the winner against both computer players
    def determine_winner(player, computer):
        if player == computer:
            return "Tie"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "Win"
        else:
            return "Lose"

    result1 = determine_winner(player, computer1)
    result2 = determine_winner(player, computer2)

    # Check if the player won against both computers
    if result1 == "Win" and result2 == "Win":
        print("You Win Against Both Computers!")
    elif result1 == "Tie" and result2 == "Tie":
        print("It's a Tie with Both Computers!")
    elif result1 == "Tie":
        print("You Tie with Computer 1!")
    elif result2 == "Tie":
        print("You Tie with Computer 2!")
    elif result1 == "Win":
        print("You Win Against Computer 1, but Lose to Computer 2!")
    elif result2 == "Win":
        print("You Win Against Computer 2, but Lose to Computer 1!")
    else:
        print("You Lose to Both Computers!")

    if input("Play again? (yes/no): ").lower() != "yes":
        running = False

print("Thanks for Playing!")

    



