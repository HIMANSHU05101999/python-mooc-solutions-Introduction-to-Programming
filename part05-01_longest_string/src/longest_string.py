# Write your solution here
def longest_my_function(user_input: list):
    sorted_list=[]
    list_len=[]
    for i in range (0, len(user_input)):
        list_len.append(len(user_input[i]))
    sorted_list=sorted(list_len)

    temp=sorted_list[-1]

    for j in range (0,len(list_len)-1):
        if list_len[j]==temp:
            break
    return (user_input[j])

def longest(user_input: list):
    temp=""
    for item in user_input:
        if len(item)>len(temp):
            temp=item
    return (temp)



if __name__=="__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))







    