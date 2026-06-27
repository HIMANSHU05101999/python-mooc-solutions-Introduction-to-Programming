# Write your solution here
def range_of_list(list):
    i=0
    large=small=list[0]
    while i<len(list):
        if large<list[i]:
            large=list[i]
        if small>list[i]:
            small=list[i]
        i+=1
    return (large-small)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)