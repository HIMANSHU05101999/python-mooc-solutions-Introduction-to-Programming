# Write your solution here
import string
import random
def generate_strong_password_my(num: int, boolean1: bool, boolean2: bool):
    char=len(string.ascii_lowercase)
    number=len(string.digits)
    sp_char=len("!?=+-()#")
    use_char=string.ascii_lowercase+string.digits+"!?=+-()#"
    use_char2=string.ascii_lowercase+"!?=+-()#"
    pw=""
    while len(pw)<num:
        if boolean1==True and boolean2==True:
            pw+=use_char[random.randint(0,(char+number+sp_char)-1)]
        elif boolean1==True and boolean2==False:
            pw+=use_char[random.randint(0,(char+number)-1)]
        elif boolean1==False and boolean2==True:
            pw+=use_char2[random.randint(0,(char+sp_char)-1)]
        else:
            pw+=use_char[random.randint(0,(char)-1)]
    return (pw)

def generate_strong_password_other(num: int, boolean1: bool, boolean2: bool):
    pw=""
    for i in range(num):
        if boolean1==True and boolean2==True:
            pw+=random.choice(string.ascii_lowercase+string.digits+"!?=+-()#")
        elif boolean1==True and boolean2==False:
            pw+=random.choice(string.ascii_lowercase+string.digits)
        elif boolean1==False and boolean2==True:
            pw+=random.choice(string.ascii_lowercase+"!?=+-()#")
        else:
            pw+=random.choice(string.ascii_lowercase)
    return pw
def generate_strong_password(num: int, boolean1: bool, boolean2: bool):
    pw_list=[]
    password=""
    for i in range(num):
        if boolean1==True:
            if len(pw_list)==num:
                break
            pw_list.append(random.choice(string.digits))
            
        if boolean2==True:
            if len(pw_list)==num:
                break
            pw_list.append(random.choice("!?=+-()#"))
            
        if True:
            if len(pw_list)==num:
                break
            pw_list.append(random.choice(string.ascii_lowercase))
            random.shuffle(pw_list)
        random.shuffle(pw_list)
    
    for item in pw_list:
        password+=item
    return password

def main():
    for i in range(10):
        print(generate_strong_password(5, True, True))
if __name__=="__main__":
    main()