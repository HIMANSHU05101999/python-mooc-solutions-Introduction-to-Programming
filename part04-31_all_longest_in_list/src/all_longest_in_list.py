# Write your solution here
def all_the_longest(input_list):
    new_list=[]
    temp=0
    for item in input_list:
        if len(item)>=temp:
            temp=len(item)
    for item in input_list:
        if len(item)==temp:
            new_list.append(item)
    return new_list


if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']