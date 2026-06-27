# Write your solution here
char=input("Please type in a string:")
#char="hey"
vow="aeo"
index=0
while index<len(vow):
    #print(vow[index])
    if vow[index] in char:
        print(vow[index]+" found")
    else:
        print(vow[index]+" not found")
    index+=1