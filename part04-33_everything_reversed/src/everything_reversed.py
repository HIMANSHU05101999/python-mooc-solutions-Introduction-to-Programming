# Write your solution here
#def everything_reversed(input_list):
#    new_list=[]
#    reversed_new_list=[]
#    for i in range (0,len(input_list)):
#        temp_string=""
#        for j in range (len(input_list[i]),0,-1):
#            temp_string+=input_list[i][j-1]
#        new_list.append(temp_string)
#    for k in range(len(new_list),0,-1):
#        reversed_new_list.append(new_list[k-1])
#    return reversed_new_list

def everything_reversed(input_list):
    new_list=[]
    for item in input_list:
        new_list.append(item[::-1])
    return new_list[::-1]



if __name__=="__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)