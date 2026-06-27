# Write your solution here
limit=int(input("Limit:"))
num=0
total=0
store=""
while total<limit:
    num+=1
    total+=num
    if num==1:
        store=store+f"{num}"
    else:
        store=store+f" + {num}"

print(f"The consecutive sum: {store} = {total}")