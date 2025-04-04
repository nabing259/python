# Problem: Given a string, find the first non-repeated character.

string = input("Enter a string:\n")

for char in string:
    if string.count(char) == 1:
        print("The first non-repeated character is:", char)
        break