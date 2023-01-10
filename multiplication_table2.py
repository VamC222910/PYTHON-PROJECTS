first_num = int(input("Enter a number : "))
num = int(input("Enter a second number : "))
if first_num>num:
    print("Invalid")
    first_num =  input("Please enter a number less than second input : ")
    num = input("Enter the second number : ")
    
elif first_num<num:
    while first_num<num:
        sec_num = 1
        while sec_num <11:
            multiply = first_num*sec_num
            print(first_num,"x",sec_num,"=",multiply)
            sec_num = sec_num+ 1
        print()
        first_num = first_num + 1