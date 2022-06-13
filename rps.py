import random

counter = 5
computer_win = 0
player_win = 0


while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:    
        player = input("rock, paper, or scissors?: ").lower()
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_win += 1

        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_win += 1

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_win += 1
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_win += 1
        
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            computer_win += 1
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            player_win += 1

    counter = counter - 1    

    if counter == 0:
        if player_win > computer_win:
            print(f"Player wins the game!!")
        else:
            print(f"Computer wins the game!!")
   
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break


print("Bye!")