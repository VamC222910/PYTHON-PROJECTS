import random
count_zero = 0
count_one = 0

player_score = 0
computer_score = 0

def prediction():
    if count_zero > count_one:
        predict = 0
    elif count_one > count_zero:
        predict = 1
    else:
        predict = random.randint(0,1)
    return predict
def update_counts(player_input):
    global count_zero,count_one
    if player_input == 0:
        count_zero = count_zero + 1
    else:
        count_one = count_zero + 1
def update_score(predicted,player_input):
    global player_score,computer_score
    if predicted == player_input:
        computer_score = computer_score+1
        print("Computer Score : ",computer_score)
        print("Player Score :",player_score)
    else:
        player_score = player_score+1
        print("Computer Score : ",computer_score)
        print("Player Score : ",player_score)
def gameplay():
    valid_entries = ['0','1']
    while True:
        predicted = prediction()
        player_input = input("Enter either 0 or 1 : ")
        while player_input not in valid_entries:
            print("Invalid input!! ")
            player_input = input("Please enter either 0 or 1 : ")
        player_input = int(player_input)
        update_counts(player_input)
        update_score(predicted,player_input)
        if player_score == 10:
            print("congrats, You Won!!")
            break
        elif computer_score == 10:
            print("Back Luck, Computer Won!!")
            break
gameplay()