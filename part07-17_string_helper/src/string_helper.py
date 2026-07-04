# Write your solution here
def change_case(orig_string: str):
    return_string=""
    for letter in orig_string:
        if letter == letter.upper():
            return_string+=letter.lower()
        elif letter == letter.lower():
            return_string+=letter.upper()
        else:
            return_string+=letter
    return return_string

def split_in_half(orig_string: str):
    part1=""
    part2=""
    half_length_of_string=len(orig_string)//2
    part1=orig_string[0:half_length_of_string]
    part2=orig_string[half_length_of_string:]
    return (part1,part2)    
    
def remove_special_characters(orig_string: str):
    import string
    char=string.ascii_letters+" "+string.digits 
    return_string=""
    for letter in orig_string:
        if letter in char:
            return_string+=letter
    return return_string

if __name__=="__main__":
    def main():
        my_string = "Thi§ is a test test"
        print(change_case(my_string))
        print(split_in_half(my_string))
        print(remove_special_characters(my_string))
    main()