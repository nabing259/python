# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = "dog"
age = 2

if pet == "dog":
    if age<2:
        print("Puppy food")
    else:
        print("Dog food")
elif pet == "cat":
    if age<2:
        print("kitten food")
    else:
        print("Cat food")