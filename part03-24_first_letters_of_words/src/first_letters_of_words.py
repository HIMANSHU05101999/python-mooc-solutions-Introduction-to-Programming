# Write your solution here
string=input("Please type in a sentence:")
#string="Humpty Dumpty sat on a wall"
index=0
while index<len(string)-1:
    if index==0 or string[index-1] == " ":
        print(string[index])
        index+=1
    else:
        index+=1
        
    
    


    