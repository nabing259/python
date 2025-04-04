# Problem: Check if a number is prime.

number = int(input("Enter a number:\n"))
isPrime = True

if number>1:
    for i in range(2, number):
        print(i,"-----------")
        if number % i == 0:
            isPrime = False
            break

if isPrime:
    print(number,"is a prime number")
else :
    print(number,"is not a primer number")