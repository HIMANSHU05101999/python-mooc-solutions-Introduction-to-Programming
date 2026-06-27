# Write your solution here
def search(dictionary: dict):
    name=input("name:")
    if name in dictionary:
        print(dictionary[name])
    else:    
        print("no number")

def add(dictionary: dict):
    string=""
    name=input("name:")
    if name not in dictionary:
        num=input("number:")
        dictionary[name] = num
        print("ok!")
    elif name in dictionary:
        string=dictionary[name]
        num=input("number:")
        string+= "\n" + num
        dictionary[name] = string
        print("ok!")

def quit():
    print("quitting...")

def main():
    phonebook={}
    while True:
        user_input=int(input("command (1 search, 2 add, 3 quit):"))
        if user_input==1:
            search(phonebook)
        elif user_input==2:
            add(phonebook)
        elif user_input==3:
            quit()
            break

main()

