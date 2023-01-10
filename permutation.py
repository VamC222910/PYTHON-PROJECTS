# In this program we will ask the user to enter the number of switches and calculate the possible outcomes that can come from those many number of switches(on/off)
user_input = int(input("Enter the number of Switches"))
max_possible = 2  #Here max_possible denotes the maximum possible outcomes of 1 switc
i = 1 # i is used to set the condition of while loop and it will keep incrementing unless all the switches are over
power = 1 # power variable is futehr used to store the result
while i<=user_input :
    power = max_possible*power
    i = i+1
    print("Total number of outcomes : ",power)
    break