# Write your solution here
num=1
i=1
while i<=num:
    num=int(input("Please type in a number:"))
    if num<=0:
        print("Thanks and bye!")   
        break
    j=0
    k=1
    while j<num:
        j+=1
        k*=j
    print(f"The factorial of the number {num} is {k}")
#print("Thanks and bye!")   
