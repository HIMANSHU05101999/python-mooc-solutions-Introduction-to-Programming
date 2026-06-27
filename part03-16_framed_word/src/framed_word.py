# Write your solution here

word=input("Word:")
lenght=int((28-(len(word)))/2)
finallen=lenght
if len(word)%2!=0:
    finallen+=1
print("*"*30)
print("*"+" "*(lenght)+word+" "*(finallen)+"*")
print("*"*30)
    