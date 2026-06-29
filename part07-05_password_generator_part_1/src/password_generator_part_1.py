# Write your solution here
import random
import string

def generate_password(num: int):
    char=string.ascii_lowercase
    length=len(char)
    pw_string=""
    while len(pw_string)<num:
        pw_string+=char[random.randint(0,length-1)]
    return pw_string

def main():
    for i in range(10):
        print(generate_password(2))
if __name__=="__main__":
    main()