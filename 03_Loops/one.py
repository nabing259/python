# Problem: Given a list of numbers, count how many are positive.

numbers = list(map(int, input("Enter numbers: ").split(",")))
count = 0
for number in numbers:
    if number>=0:
        count += 1

print("Total number of positive numbers are: ", count)