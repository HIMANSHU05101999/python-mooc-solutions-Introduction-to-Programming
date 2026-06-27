# Write your solution here
i=0
word=[]
while True:
    value=input("Word:")
    i+=1
    if value in word:
        break
    word.append(value)
print(f"You typed in {i-1} different words")