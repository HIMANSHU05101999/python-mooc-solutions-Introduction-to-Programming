# Write your solution here

previousword=""
story=""
while True:
    word=input("Please type in a word")
    
    if word=="end":
        break
    
    if word==previousword:
        break
    previousword=word
    story+=word + " "
print(story)


