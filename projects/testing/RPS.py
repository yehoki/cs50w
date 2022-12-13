import random

user_wins = 0
computer_wins = 0

selections = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_choice == "q":
        quit()

    if user_choice not in selections:
        continue

    computer_number = random.randint(0,2)
    #r:0, p:1, s:2
    print("The computer picked ",format(selections[computer_number]))
    
    comp_choice = selections[computer_number]
    if user_choice == "rock":
        if comp_choice == "rock":
            print("It's a draw!")
        elif comp_choice == "paper":
            print("You lost!")
            computer_wins +=1
        else:
            print("You won!")
            user_wins += 1

    if user_choice == "paper":
        if comp_choice == "rock":
            print("You won!")
            user_wins +=1
        elif comp_choice == "paper":
            print("It's a draw!")
        else:
            print("You lost!")
            computer_wins += 1
    if user_choice == "scissors":
        if comp_choice == "rock":
            print("You lost!")
            computer_wins +=1
        elif comp_choice == "paper":
            print("You won!")
            user_wins +=1
        else:
            print("It's a draw!")
    print(user_wins, computer_wins)