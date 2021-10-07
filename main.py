import random

turns = ["rock", "paper", "scissors"]
computer_turn = random.choice(turns)
human_turn = input("Enter human turn: ").lower()

print(f"Computer: {computer_turn} VS. Human: {human_turn}")

if computer_turn == human_turn:
    print("Draw!")

elif ((computer_turn == "paper" and human_turn == "rock") or 
        (computer_turn == "scissors" and human_turn == "paper") or 
        (computer_turn == "rock" and human_turn == "scissors")):
    print("Computer wins!")

else:
    print("Human wins!")