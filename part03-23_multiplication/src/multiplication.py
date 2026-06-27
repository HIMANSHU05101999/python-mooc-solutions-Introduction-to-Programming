# Write your solution here
inp=int(input("Please type in a number:"))
num=1
while num<=inp:
    i=0
    while i<inp:
        i+=1
        print(f"{num} x {i} = {num*i}")
        
    num+=1