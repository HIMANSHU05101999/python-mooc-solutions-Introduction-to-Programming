string = "once upon time"
index=0
count=0
first_index=0
while index<len(string)-1:
    index+=1
    #print(index,first_index,count)
    if string[index]==" ":
        count+=1
        #print(string[0:index])
    print(index,first_index,count)
    first_index=count

    
       