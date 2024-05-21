items = ['apple', 'banana', 'orange', 'apple', 'mango']

set_items = set()

for i in items:
    if i in set_items:
        print("Duplicate found: ", i)
        break
    set_items.add(i)