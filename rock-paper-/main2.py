# Player playing with one computer

import random

#from symbol import comp_iter

options = ("rock","paper","scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors) : ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer :
        print("Its a Tie!")
    elif player == "rock" and computer == "scissors" :
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win !")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")

    if not input("Play again ? (yes/no)").lower() == "yes":
        running = False

print("Thanks for Playing!")
    