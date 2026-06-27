# Write your solution here
def add_item(num):
    item=1
    list=[]
    value=0
    while num>0:
        value=int(input(f"Item {item}:"))
        list.append(value)
        item+=1
        num-=1
    print(list)

if __name__=="__main__":
    num=int(input("How many items:"))
    add_item(num)