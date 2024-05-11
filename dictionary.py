dict = {"one": 1, "two": 2, "three": 3}
print(dict)
for i in dict.keys():
    if(i == 'one'):
        dict[i]='seven'

print(dict)