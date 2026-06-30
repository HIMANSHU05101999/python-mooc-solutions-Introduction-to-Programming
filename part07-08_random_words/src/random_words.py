# Write your solution here
import random
import pathlib
def words(n: int, beginning: str):
    file_name=pathlib.Path(__file__).parent/"words.txt"

    word_list=[]
    with open(file_name) as file:
        for word in file:
            word=word.strip()
            if word.startswith(beginning):
                word_list.append(word)
    return_list=[]
    if len(word_list)<n:
            raise ValueError
    while len(return_list)<n:
        word_to_add=random.choice(word_list)
        if word_to_add not in return_list:
            return_list.append(word_to_add)
    return (return_list)
           

def main():
    word_list = words(7, "of")
    for word in word_list:
        print(word)
if __name__=="__main__":
    main()