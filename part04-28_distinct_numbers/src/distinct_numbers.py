# Write your solution here
def sorting(input_list):
    for i in range(0,len(input_list)-1):  
        #print(f"this is i {i}")  
        #temp=0 
        for j in range(0,len(input_list)-1):
            if input_list[j]>input_list[j+1]:
                temp=input_list[j]
                input_list[j]=input_list[j+1]
                input_list[j+1]=temp
                #print(f"this is j {j}")
                #print(input_list)
    return input_list

#def distinct_numbers(input_list):
    input_list=sorting(input_list)
    for i in range(0,len(input_list)):
        count=0
        len_list=len(input_list)-1-count
        for j in range(0,len_list):
            if input_list[j]==input_list[j+1]:
                count+=1
                input_list.remove(input_list[j])
                break
    return input_list

def distinct_numbers(input_list):
    new_list=[]
    for i in range(0,len(input_list)):
        if input_list[i] not in new_list:
            new_list.append(input_list[i])
    return sorting(new_list)
    
if __name__=="__main__":
    my_list = [3, 2, 2, 1]
    print(distinct_numbers(my_list)) 


