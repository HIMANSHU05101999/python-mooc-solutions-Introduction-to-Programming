# Write your solution here
count=0
add=0

positive=0
negative=0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num=int(input("Number:"))
    if num>0:
        positive=positive+1
    if num<0:
        negative=negative+1
    if num==0:
        break
    count=count+1
    add=add+num
print("... the program asks for numbers")
print("Numbers typed in",count)
print("The sum of the numbers is",add)
print("The mean of the numbers is",add/count)
print("Positive numbers",positive)
print("Negative numbers",negative)