import random

while True:
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Play against the computer")
    print("2. Play against another person")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("You are playing against the computer.")
        score = int(input("Enter the score you want to play until: "))
        player_score = 0
        computer_score = 0
        while player_score < score and computer_score < score:
            player_choice = input("Enter your choice (rock/paper/scissors): ")
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print("The computer chose", computer_choice)

            if player_choice == computer_choice:
                print("It's a tie!")
            elif player_choice == "rock" and computer_choice == "scissors":
                print("You win!")
                player_score += 1
            elif player_choice == "paper" and computer_choice == "rock":
                print("You win!")
                player_score += 1
            elif player_choice == "scissors" and computer_choice == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1

            print("Score: Player", player_score, "- Computer", computer_score)

        if player_score > computer_score:
            print("Congratulations! You won the game!")
        else:
            print("Sorry, you lost the game.")

    elif choice == "2":
        print("You are playing against another person.")
        score = int(input("Enter the score you want to play until: "))
        player1_score = 0
        player2_score = 0
        while player1_score < score and player2_score < score:
            player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ")
            player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ")

            if player1_choice == player2_choice:
                print("It's a tie!")
            elif player1_choice == "rock" and player2_choice == "scissors":
                print("Player 1 wins!")
                player1_score += 1
            elif player1_choice == "paper" and player2_choice == "rock":
                print("Player 1 wins!")
                player1_score += 1
            elif player1_choice == "scissors" and player2_choice == "paper":
                print("Player 1 wins!")
                player1_score += 1
            else:
                print("Player 2 wins!")
                player2_score += 1

            print("Score: Player 1", player1_score, "- Player 2", player2_score)

        if player1_score > player2_score:
            print("Congratulations! Player 1 won the game!")
        else:
            print("Congratulations! Player 2 won the game!")

    elif choice == "3":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")