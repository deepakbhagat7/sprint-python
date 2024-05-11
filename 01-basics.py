a = [5, 7, 8, 6, 14, 6]
print(a[::2])

import math

print(math.floor(3.5))

print(math.trunc(-2.9))

print(math.factorial(7))


# random library features
import random as r

random_no = r.random()
# randint gives you random integer between two ranges
rand_no = r.randint(1,10)

print(rand_no)

print(random_no)

# random choice would be given from an array via random.choice keyword

list = ['one', 'two', 'three', 'four']
print(r.choice(list))

# we can shuffle the array using shuffel method
r.shuffle(list)

print(list)

val = (0.1 + 0.1 + 0.1) - 0.3
print(val)
# output is 5.551115123125783e-17 so in order to solve this problem we use decimal library

from decimal import Decimal
myDec = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(myDec)

# similarly we can import fractions

from fractions import Fraction
print((2.7+2.7+2.7)-8.1)
# output is 1.7763568394002505e-15 which is wrong  so in order to solve this problem we use fraction library
myFra = Fraction(2,7) + Fraction(2,7) + Fraction(2,7)
print(myFra)