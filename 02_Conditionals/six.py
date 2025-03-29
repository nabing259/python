# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = eval(input("What is the distance? \n"))

if distance<3:
    print("Go for a Walk.")
elif distance>=3<=15:
    print("Go for a Bike bro.")
else :
    print ("Go for a CAR bro.")