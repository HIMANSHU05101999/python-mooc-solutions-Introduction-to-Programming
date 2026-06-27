# Write your solution here
word=input("Please type in a word:")
char=input("Please type in a character:")
a=word.find(char)
new=word[a:a+3]
if len(new)>=3:
    print(new)
