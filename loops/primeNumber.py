# check if a number is prime number or not
num = int(input("Enter a number: "))

# for i in range(2, num):
#     if num%i == 0:
#         print("Not a prime number")
#         break
#     else :
#         print("Number is Prime")
#         break

# another approach

is_prime = True
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
if is_prime:
    print("Number is Prime")
else:
    print("Number is Not Prime")
