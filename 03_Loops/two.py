# Problem: Calculate the sum of even numbers up to a given number n.
n = int(input("Enter a number: \n"))
sum_of_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_of_even += i

print("Sum of Even numbers = ", sum_of_even)