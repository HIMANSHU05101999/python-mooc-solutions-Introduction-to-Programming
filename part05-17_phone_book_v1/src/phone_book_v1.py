# Write your solution here
phone_book={}
while True:
    user_inp=int(input("command (1 search, 2 add, 3 quit)"))
    if user_inp==1:
        name=input("name:")
        if name in phone_book:
            print(f"{phone_book[name]}")
        else:
            print("no number")
    elif user_inp==2:
        name=input("name:")
        num=input("number:")
        phone_book[name]=num
        print("ok!")
        
    elif user_inp==3:
        print("quitting...")
        break