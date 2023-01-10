import random
count_rock = 0
count_paper = 0
count_scissor = 0

def update_count(user_input):
    global count_rock,count_paper,count_scissor
    if user_input == 0:
        count_rock = count_rock + 1
    elif user_input == 1:
        count_paper = count_paper + 1
    elif user_input == 2:
        count_scissor = count_scissor + 1

def predict():
    if count_rock > count_paper and count_rock > count_scissor:
        pred = 0
    elif count_paper > count_rock and count_paper > count_scissor:
        pred = 1
    elif count_scissor > count_rock and count_scissor > count_paper:
        pred = 2
    else:
        pred = random.randint(0,2)
    return pred

player_score = 0
computer_score = 0

def update_Scores(user_input):
    global player_score,computer_score
    pred = predict()
    if user_input == 0:
        if pred == 0:
            print("\n You played ROCk, Computer Played ROCK. ")
            print("\n Computer Score : ",computer_score,"\n Player Score : ",player_score)
        elif pred == 1:
            print("\n You played ROCK, Computer Played PAPER. ")
            computer_score += 1
            print("\n Computer Score : ",computer_score,"\n Player Score : ",player_score)
        elif pred == 2:
            print("\n You played ROCK, Computer played Scissor. ")
            computer_score += 1
            print("\n Computer Score : ",computer_score,"\n Player Score : ",player_score)
    elif user_input == 1:
        if pred == 1:
            print("\nYou played PAPER , computer played PAPER.")
            print("\nComputer Score: ", computer_score, "\nYour Score: ", player_score)
        elif pred == 0:
            print("\nYou played PAPER, computer played ROCK.")
            player_score += 1
            print("\nComputer Score: ", computer_score, "\nYour Score: ", player_score)
        else:
            print("\nYou played PAPER, computer played SCISSORS.")
            computer_score += 1
            print("\nComputer Score: ", computer_score, "\nYour Score: ", player_score)
    else:
        user_input == 2
        if pred == 2:
            print("\nYou played SCISSORS , computer played SCISSORS.")
            print("\nComputer Score: ", computer_score, "\nYour Score: ", player_score)
        elif pred == 0:
            print("\nYou played SCISSOR, computer played ROCK.")
            computer_score += 1
            print("\nComputer Score: ", computer_score, "\nYour Score: ", player_score)
        else:
            print("\nYou played SCISSORS, computer played PAPER.")
            player_score += 1
            print("\nComputer Score: ", computer_score, "\nYour Score: ", player_score)

valid_entries = ['0','1','2']
while True:
    user_input  = input("Enter either 0 for ROCK, 1 for PAPER and 2 for SCISSORS : ")
    while user_input not in valid_entries:
        print("Invalid Input!!")
        user_input  = input("Enter either 0 for ROCK, 1 for PAPER and 2 for SCISSORS : ")
    user_input = int(user_input)
    update_Scores(user_input)
    update_count(user_input)
    if computer_score == 10:
        print("Computer Won!!")
        break
    elif player_score == 10:
        print("You Won")
        break
