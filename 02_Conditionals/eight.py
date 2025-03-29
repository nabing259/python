# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: \n")

if password.len<6:
    print("Your password is weak")
elif password.len<=10:
    print("Your password is Medium")
else:
    print("Your password is Strong")