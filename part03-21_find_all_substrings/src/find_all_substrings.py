# Write your solution here
word=input("Please type in a word:")
char=input("Please type in a character:")
a=word.find(char)
while a<len(word) and len(word[a:a+3])==3:
    if char==word[a]:
        print(word[a:a+3])
        a+=1
    else:
        a+=1
    
    


