# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = eval(input("Enter Your Age: \n"))
day = input("Enter Today's Day: \n")

ticket_price = 8 if age<18 else 12

if day == "Wednesday":
    ticket_price -= 2

print("Ticket Price is $",ticket_price)
