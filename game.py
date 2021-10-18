
# IMPORTING THE RANDOM MODULE TO USE THE RANDIT METHOD
from random import randint

# INITIALISING PLAYER'S SCORE AND COMPUTER'S SCORE TO 0
computer_score = 0
player_score = 0

print("\n")

print("Let's start with the Game of Rock, Paper and Scissors :) \n\n")

while True:

    player = input("Make your move: ").lower()  # CONVERTING STRING VALUE TO LOWER-CASE

    random_number = randint(0, 2)  # ASSIGNING A RANDOM INTEGER FOR THE GAME OPTIONS
    if random_number == 0:
        computer = "rock"
    elif random_number == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer}")

    if player == computer:  # WORKING OUT THE DIFFERENT SCENARIOS OF THE GAME
        print("it's a tie! \n")
    elif player == "rock":
        if computer == "scissors":
            print("player wins \n")
            player_score += 1
        elif computer == "paper":
            print("computer wins \n")
            computer_score += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins \n")
            player_score += 1
        elif computer == "scissors":
            print("computer wins \n")
            computer_score += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins \n")
            player_score += 1
        elif computer == "rock":
            print("computer wins \n")
            computer_score += 1
    else:
        print("Please enter a valid move!")

    result = print(
        "Result: Computer = ", computer_score, " vs", " Player = ", player_score  # SHOWING THE SCORES FOR PLAYER VS COMPUTER 
    )
    

    Play_again = input("Wanna play again?(Yes/No):").lower()  # GIVING AN OPTION TO STOP OR RESUME THE GAME 
    if Play_again != "Yes".lower():
        print("Thank you for playing my game! \n")
        if computer_score > player_score:    # DECLARING THE WINNER 
          print("Computer won, you can never beat computers, hard luck!")
        elif computer_score == player_score:
          print("You are as smart as the computer in rock paper scissors!")
        else:
          print("You won, You defeated the machine, great job!")
        break