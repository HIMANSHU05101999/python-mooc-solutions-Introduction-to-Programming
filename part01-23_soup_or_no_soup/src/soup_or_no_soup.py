# Write your solution here
name=input("Please tell me your name: ")
if name=="Jerry":
    print("Next please!")
else:
    portion=int(input("How many portions of soup? "))
    total=portion*5.90    
    print(f"The total cost is {total}\nNext please!")