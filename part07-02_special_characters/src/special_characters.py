# Write your solution here
import string

def separate_characters_my_sol(my_string: str):
    letter=""
    punc=""
    rem=""
    for item in my_string:
        if item in string.ascii_letters:
            letter+=item
    for item in my_string:
        if item in string.punctuation:
            punc+=item
    combined=letter+punc
    for item in my_string:
        if item not in combined:
            rem+=item
    return (letter,punc,rem)

def separate_characters(my_string: str):
    letter=""
    punc=""
    rem=""
    for item in my_string:
        if item in string.ascii_letters:
            letter+=item
        elif item in string.punctuation:
            punc+=item
        else:
            rem+=item
    return(letter,punc,rem)

def main():
    parts=separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
if __name__=="__main__":
    main()