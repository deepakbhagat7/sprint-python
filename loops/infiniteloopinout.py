# take input from user until user hasn't enter value between 1 to 10

while True:
    num = int(input("Enter the number b/w 1 to 10: "))
    if 1 <= num <= 10:
        print("Valid input found")
        break
    else :
        print("Invalid Input")
