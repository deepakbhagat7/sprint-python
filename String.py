string = "0123456789"
ans = string[0:10:3]
print(ans)

s1 = "   deep is a good boy "
print(s1)

print(s1.strip())
print(s1.split())
s2 = "lemon, ginger, ice, green"
print(s2.split())  # it will split by spaces as you havent give any instructions on the slpit paramenter
print(s2.split(', '))  # here it will split on the basis of a , and ' ' as you have passed in the split parameter

# replacing
s3 = "Happy Number"

y = s3.replace("Happy", "sad")
print(y)
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

# count
s4 = "I love sejal sejal sejal sejal"
print(s4.count('sejal'))
# find
s5 = "I love sejal"
print(s5.find('sejal'))

# formatting with placeholder
orderItem = "chicken burger"
qty = 2
order = "I want to order {} {} immediately" #{} this is not dictionary this acts as a placeholder

print(order.format(qty, orderItem))

# conversion of array into string using join keyword

list = ['hi', 'I', 'am', 'Deep']
print(list)
print("".join(list)) #not space seperated
print(" ".join(list)) #space seperated

arr = [x**2 for x in range(10)]
print(arr)

