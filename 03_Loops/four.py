# Problem: Reverse a string using a loop.

string = input("Enter a String:\n")

reverse_string = ""

for char in string:
    reverse_string = char+reverse_string

print(reverse_string)