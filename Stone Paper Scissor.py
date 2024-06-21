import random

print("___________________________WELCOME TO STONE PAPER AND SCISSOR WORLD___________________________")

player1 = 0
player2 = 0

while True:

    choice = ["stone","paper","scissor"]
    player1_choice = random.choice(choice)



    player2_choice = input("Enter your choice (stone/paper/scissor): ").lower()

    if player1_choice == player2_choice:
        print("Draw")
    else:
        if player1_choice == "stone" and player2_choice == "scissor":
            print(f"Computer: {player1_choice}")
            print(f"Player1 wins because {player1_choice} beats {player2_choice}")
            player1 += 1
        elif player1_choice == "stone" and player2_choice == "paper":
            print(f"Computer: {player1_choice}")
            print(f"You Win because {player2_choice} beats {player1_choice}")
            player2 += 1

        elif player1_choice == "paper" and player2_choice == "scissor":
            print(f"Computer: {player1_choice}")
            print(f"You Win because {player2_choice} beats {player1_choice}")
            player2 += 1
        elif player1_choice == "paper" and player2_choice == "stone":
            print(f"Computer: {player1_choice}")
            print(f"Player1 wins because {player1_choice} beats {player2_choice}")
            player1 += 1

        elif player1_choice == "scissor" and player2_choice == "stone":
            print(f"Computer: {player1_choice}")
            print(f"You Win because {player2_choice} beats {player1_choice}")
            player2 += 1
        elif player1_choice == "scissor" and player2_choice == "paper":
            print(f"Computer: {player1_choice}")
            print(f"Player1 wins because {player1_choice} beats {player2_choice}")
            player1 += 1

        print("___________Current Result___________")
        print(f"Computer: {player1}")
        print(f"Player: {player2}")

    x = input("Do you want to end the game (y/n): ")
    if x == "y":
        print("_________________THANK YOU_________________")
        break 
