import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player_score = 0
cpu_score = 0
while True:
    player = input("Please choose rock, paper, or scissors")
    if player == computer:
        print("draw")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            cpu_score += 1
        elif computer == "scissors":
            print("You win!", player, "smashs", computer)
            player_score += 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
            cpu_score += 1
        elif computer == "rock":
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashs", player)
            cpu_score += 1
        elif computer == "paper":
            print("You win!", player, "cut", computer)
            player_score += 1
    elif player == "end":
        print("End of Game and the final scores are:")
        print(f"CPU:{cpu_score}")
        print(f"player:{player_score}")
        break
    else:
        print("Invalid input")
    computer = random.choice(choices)