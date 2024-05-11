dict = {"one": 1, "two": 2, "three": 3}
print(dict)
for i in dict.keys():
    if(i == 'one'):
        dict[i]='seven'

print(dict)


# number = input()
# print(number)
list = input('Enter No').split()
list = [int(i) for i in list]
print(list)
