import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user == "exit":
        print("Game Over!")
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")