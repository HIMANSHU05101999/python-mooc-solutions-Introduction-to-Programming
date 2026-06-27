from math import sqrt
# Write your solution here
while True:
    num=int(input("Please type in a number:"))
    if num<0:
        print("Invalid number")
    elif num>0:
        print(sqrt(num))
    else:
        break

print("Exiting...")
