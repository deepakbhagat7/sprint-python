dict = {"one": 1, "two": 2, "three": 3}
print(dict)
for i in dict.keys():
    if(i == 'one'):
        dict[i]='seven'

print(dict)

# taking user input as number
# number = input()
# print(number)

# taking user input in list
# list = input('Enter No').split()
# list = [int(i) for i in list]
# print(list)

# if the element is present in dictionary or not
if "one" in dict:
    print('yes')
else:
    print('no')
#  adding elements in a dictionary
dict["four"] = 4

print(dict)
