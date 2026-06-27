# Write your solution here
list=[1,2,3,4,5]
index=0
value=0
while True:
    index = int(input("Index:"))
    if index<0:
        break
    else:
        value = int(input("New value:"))
        list[index]=value
        print(list)
   


