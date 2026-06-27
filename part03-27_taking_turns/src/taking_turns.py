# Write your solution here
num=int(input("Please type in a number:"))
i=0
j=num
while i<num:
    i+=1
    j-=1
    if i<=(num+1)/2:
        print(i)
    if j>=num/2:
        print(j+1)
        