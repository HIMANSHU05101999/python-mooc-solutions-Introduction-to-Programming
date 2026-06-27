# Write your solution here
num=int(input("Please type in a positive integer: "))

for i in range(-num,num+1):
    if i==0:
        print(end="")
    else:
        print(i)