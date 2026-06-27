# Write your solution here
def squared(string,num):
    row=0
    sentence=string*num*num
    index=0
    while row<num:
        row+=1
        index=(row-1)*num
        print(sentence[index:index+num])
        

if __name__=="__main__":
    squared("aybabtu",5)