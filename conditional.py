# # classify a person's age group: Child(<13), Teenager(13-19), Adult(20-25), Senoir(60+)
# age = int(input(" Enter your age\n"))
#
# if age<13:
#     print("Child")
# elif age>=13 and age<20:
#     print("Teenager")
# elif age>=20 and age<60:
#     print("Adult")
# else:
#     print("Senior citizen")

#     Movie tickets are priced based on the age 120 for adults(18 and over), 80 for chikdren everyone geta a dicouunt on wednesday
#
# age = int(input("Enter age:\n"))
# day = input("Enter the day:\n")
# price = 0
# if age < 18:
#     price = 80
# elif age >= 18:
#     price = 120
#
# if day.lower() == 'wednesday':
#     price -= 20
# print(price)
#
# # using ternery operator
#
# price = 120 if age >= 18 else 8
# print(price)


# Assign a letter grade based on student score
# A(90-100), B(80-89), C(70-79), D(60-69),F(below 60)
# marks = 800
# if marks >= 101:
#     print("Enter valid value less than 101")
#     exit(0)
#
# if marks >= 90 and marks <= 100:
#     print("A")
# elif marks >= 80 and marks < 90:
#     print("B")
# elif marks >= 70 and marks < 80:
#     print("C")
# elif marks >= 60 and marks < 70:
#     print("D")
# else:
#     print("F")

# distance = 5
#
# if distance < 3:
#     transport = "Walk"
# elif distance <= 15:
#     transport = "Bike"
# else:
#     transport = "Car"
# print(transport)


# Leap year program

year = 4000

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Non Leap Year")
