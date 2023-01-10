#Multiply a number with the previous number
number = int(input("Enter a number : "))
def multiplier(n):
    if n<0:
        print("sorry the number cannot be negative ")
        number = input("Please enter a positive number : ")
    elif n ==0:
        print("The Result is 1")
        number = input("Please enter a positive number : ")
    else:
        mult = 1
        while n>0:
            mult = mult*n
            n = n-1
            return (mult)
multiplier(number)