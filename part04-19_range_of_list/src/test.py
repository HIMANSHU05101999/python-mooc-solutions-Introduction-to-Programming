def sorted_list(inp_list):
    temp=0
    for i in range (0,len(inp_list)-1):
        
        j=0
        while j<len(inp_list)-1:
            if inp_list[j]>inp_list[j+1]:
                temp=inp_list[j+1]
                inp_list[j+1]=inp_list[j]
                inp_list[j]=temp
            j+=1
    return inp_list

def second_largest(use_list):
    sortedlist=sorted_list(use_list)
    listlenght=len(sortedlist)-1
    for i in range (listlenght,0,-1):
        if sortedlist[i]>sortedlist[i-1]:
            return (sortedlist[i-1])


if __name__=="__main__":
    my_list=[4,3,3,6,1,7,4,3,2,5,7]
    print(second_largest(my_list))

