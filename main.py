import random

turns = ["rock", "paper", "scissors"]


while True:
    computer_turn = random.choice(turns)

    while True:
        human_turn = input("Enter human turn: ").lower()
        if human_turn == "rock" or human_turn == "paper" or human_turn == "scissors":
            break
        else:
            print("Select only from rock, paper or scissors")

    print(f"Computer: {computer_turn} VS. Human: {human_turn}")

    if computer_turn == human_turn:
        print("Draw!")

    elif ((computer_turn == "paper" and human_turn == "rock") or 
            (computer_turn == "scissors" and human_turn == "paper") or 
            (computer_turn == "rock" and human_turn == "scissors")):
        print("Computer wins!")

    else:
        print("Human wins!")