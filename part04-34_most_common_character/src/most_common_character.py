# Write your solution here
def most_common_character_while_loop(string):
    index=0
    count=0
    temp=0
    stringindexed=""
    while index<len(string):
        j=0
        while j<len(string):
            if string[index]==string[j]:
                count+=1
            j+=1
        if temp<count:
            stringindexed=string[index]
        #print(string[index],count,temp)
        #print(stringindexed)
        index+=1
        temp=count
        count=0
    return (stringindexed)

def most_common_character_for_loop(string):
    count=0
    temp=0
    stringindexed=""
    for i in range (0,len(string)):
        for j in range (0,len(string)):
            if string[i]==string[j]:
                count+=1  
        if temp<count:
            temp=count
            stringindexed=string[i]  
        count=0
    return (stringindexed)


def most_common_character(input_string):
    count=0
    temp=0
    indexed_string=""
    for i in range (0,len(input_string)):
        count=input_string.count(input_string[i])
        if count>temp:
            temp=count
            indexed_string=(input_string[i])
    return indexed_string


if __name__=="__main__":
    first_string = "abc"
    print(most_common_character(first_string))

    second_string = "aabbbbc"
    print(most_common_character(second_string))