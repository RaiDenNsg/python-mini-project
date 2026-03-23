import random
choices = ["rock","paper","sicssors"]

while True:
    user=input("\nEnter rock, paper, or sicssors (or 'exit to quit):").lower()

    if user == "exit":
        print("Game Over!")
        break
    if user not in choices:
        print("Invalid choice!")
        continue
    computer=random.choices(choices)
    print("computer choice:",computer)

    if user==computer:
        print("It is a tie!")
    elif(user == "rock" and computer == "sicssors")or(user=="paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")