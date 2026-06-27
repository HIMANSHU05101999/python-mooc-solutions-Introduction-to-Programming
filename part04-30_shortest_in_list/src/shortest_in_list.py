# Write your solution here
def shortest(input_list):
    temp=len(input_list[0])
    shortest_string=[]
    for item in input_list:
        if len(item)<temp:
            temp=len(item)
            #print(temp)
    for item in input_list:
        if len(item)==temp:
            shortest_string=item
    return shortest_string



if __name__=="__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)