# Write your solution here
def write_append_diary():
    user_input=input("Diary entry:")
    with open("diary.txt","a") as file:
        file.write(user_input+"\n")
        print("Diary saved")

def read_diary():
    print("Entries:")
    with open("diary.txt","r") as file:
        for line in file:
            print(line)

def main():
    i=1
    while i>0 and i<3:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        i=int(input("Function:"))

        if i==1:
            write_append_diary()
        elif i==2:
            read_diary()
        elif i==0:
            print("Bye now!")
main()
