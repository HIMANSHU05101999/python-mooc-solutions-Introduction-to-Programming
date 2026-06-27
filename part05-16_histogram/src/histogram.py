# Write your solution here
def histogram(word: str):
    letter={}
    for character in word :
        if character in letter:
            letter[character]+=1
        else:
            letter[character]=1
    for key in letter:
        print(key,"*"*letter[key])
           

def main():
    histogram("aaabbb")

if __name__=="__main__":
    main()
