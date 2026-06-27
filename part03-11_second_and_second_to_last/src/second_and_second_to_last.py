# Write your solution here
char=input("Please type in a string:")
if char[1]==char[-2]:
    print(f"The second and the second to last characters are {char[1]}")
else:
    print("The second and the second to last characters are different")