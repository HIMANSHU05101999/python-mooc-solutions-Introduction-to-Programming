# WRITE YOUR SOLUTION HERE:

from string import punctuation

def read_file(filename):
    punc=punctuation
    with open (filename) as file:
        content=file.read()
        content=content.split()
    content = [word.translate(str.maketrans("", "", punc)) for word in content]
    return content

    
def most_common_words(filename: str, lower_limit: int):
    content=read_file(filename)
    return {word: content.count(word) for word in content  if content.count(word)>=lower_limit}
        

if __name__=="__main__":

    a=most_common_words("comprehensions.txt", 3)
    print(a)


#print("comprehension,".translate(str.maketrans("", "", punctuation)))