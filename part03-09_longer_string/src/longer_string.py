# Write your solution here
char1=input("Please type in string 1:")
char2=input("Please type in string 2:")

if len(char1)>len(char2):
    print(f"{char1} is longer")
elif len(char1)<len(char2):
    print(f"{char2} is longer")   
else:
    print("The strings are equally long")