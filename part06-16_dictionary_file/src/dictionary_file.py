# Write your solution here
from pathlib import Path
def read_dictionary():
    return_dict={}
    read_file=Path(__file__).parent/"dictionary.txt"
    with open(read_file) as file:
        for line in file:
            line=(line.strip().split(","))
            return_dict[line[0]]=line[1]
    return return_dict
        

def write_dictionary(key: str ,val: str):
    write_file=Path(__file__).parent/"dictionary.txt"  
    with open(write_file,"a") as file:
        file.write(f"{key},{val}\n")

def dictionary():
    
    while True:
        
        dictionary_fi_en=read_dictionary()
        print("1 - Add word, 2 - Search, 3 - Quit")
        user_input=int(input("Function:"))
        if user_input==1:
            fi_word=input("The word in Finnish:")
            en_word=input("The word in English:")
            write_dictionary(fi_word,en_word)
            print("Dictionary entry added")
        elif user_input==2:
            search_word=input("Search term:")
            for key,value in dictionary_fi_en.items():
                if search_word in key or search_word in value:
                    print(f"{key} - {value}")
        if user_input==3:
            print("Bye!")
            break

dictionary()
