# skip 5 in multiplication
n = 4

for i in range(1,11):
    if i==5:
        continue
    else:
        print(n, 'x', i, '=', n*i)