# Reverse a string using loop

str = "python"
rev_str = ""

for char in str:
    rev_str = char+rev_str
print(rev_str)

# reversed using reverse loop
rev = ""
for char in reversed(str):
    rev += char

print(rev)