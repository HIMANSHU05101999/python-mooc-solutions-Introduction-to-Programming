# Write your solution here
from pathlib import Path
from difflib import get_close_matches
def spell_check():
    user_input=input("write text:")
    #user_input="this is acually a good and usefull program"
    user_input_list=user_input.strip().split(" ")
    wordlist=[]
    word_list=Path(__file__).parent/"wordlist.txt"
    with open(word_list) as file:
        for line in file:
            line=line.strip()
            wordlist.append(line)
    #print(wordlist)  
    #print(user_input_list)
    updated_list=[]
    wrong_list=[]
    suggested_dict={}
    for word in user_input_list:
        if word.lower() in wordlist:
            updated_list.append(word)
        else:
            updated_list.append('*'+word+'*')
            wrong_list.append(word)
    #print(updated_list)
    #print(wrong_list)
    for word in wrong_list:
        suggested_dict[word]=get_close_matches(word,wordlist)
    #print(suggested_dict)
    updated=" ".join(updated_list)
    print(updated)
    print("suggestions:")
    for key,val in suggested_dict.items():
        keyval=", ".join(val)
        print(key+':',keyval)

spell_check()

   