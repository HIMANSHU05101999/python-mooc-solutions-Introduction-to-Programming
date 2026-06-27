# Write your solution here
list=[]
print(f"The list is now {list}")
value=0
while True:
    choice=input("a(d)d, (r)emove or e(x)it:")
    if choice=="d":
        value+=1        
        list.append(value)
        print(f"The list is now {list}")
    elif choice=="r":
        list.remove(value)
        value-=1
        print(f"The list is now {list}")
    else:
        print("Bye!")
        break
    
    
