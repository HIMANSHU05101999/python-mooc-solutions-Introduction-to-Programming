# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    if len(pic)!=11:
        return False
    
    control_char="0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    cent_marker={"+":"18",
                 "-":"19",
                 "A":"20"
                }
    year=0
    if pic[6] in cent_marker:
        year=int(cent_marker[pic[6]]+pic[4:6])

    month=int(pic[2:4])
   
    day=int(pic[:2])
   
    control_char_chk_var=int(pic[:6]+pic[7:10])%31
    control_chk=str(control_char[control_char_chk_var])
    
    try:
        if datetime(year,month,day):
            if control_chk==(pic[-1]):
                return True
            else:
                return False
    except ValueError:    
        return False
    
def main():
    is_it_valid("230827-906F")
    is_it_valid("120488+246L")
    is_it_valid("310823A9877")
if __name__=="__main__":
    main()