# Fix the program
points = int(input("How many points are on your card? "))
if points <= 99:
    bonus = 1.1
    print("Your bonus is 10 %")

if points > 99:
    bonus = 1.15
    print("Your bonus is 15 %")

points*=bonus

print("You now have", points, "points")