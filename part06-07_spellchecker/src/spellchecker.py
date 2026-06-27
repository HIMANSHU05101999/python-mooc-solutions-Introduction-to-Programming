# write your solution here
def read_file(file_name: str):
    word_list=[]

    with open(file_name) as file:
        for item in file:
            word=item.strip()
            word_list.append(word)

    return(word_list)

def spell_checker(string: str):
    string_list=(string.split(" "))
    
    word_list=read_file("wordlist.txt")
    
    
    updated_string=[]
    
    for item in string_list:
        if item.lower() in word_list:
            updated_string.append(item)
        else:
            updated_string.append(f"*{item}*")
    
    
    new_string=""

    for i in range(len(updated_string)):
        if i==0:
            new_string+=updated_string[i]
        else:
            new_string+=" "+updated_string[i]
    
    print(new_string)


def main():
    string=input("Write text:")
    spell_checker(string)
    
main()
