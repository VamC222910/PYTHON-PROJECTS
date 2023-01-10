# In this project we will ask the user the number of WINS, DRAWS and LOSSES as input for a football team. Here we will calculate the number of points the football team has obtained so far
# A win recieves 3 points, a draw recieves 1, a loss recieves 0 points.
wins = int(input("Enter the total number of Wins : "))
draw = int(input("Enter the total number of draws : "))
loss = int(input("Enter the total number of losses : "))
total = 0
win_points = wins*3
print("Wins Points = ",win_points)
win_points = int(win_points)
total = win_points + draw
print("The toal number of points by a team is : ",total)