# Write your solution here
def length_of_longest(my_list):
    temp=len(my_list[0])
    longest_string=[]
    for item in my_list:
        if len(item)>=temp:
            temp = len(item)
            longest_string=item
    return len(longest_string)

if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)