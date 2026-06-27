# Write your solution here
def longest_series_of_neighbours(input_list):
    count=0
    temp=0
    for i in range (0,len(input_list)-1):
        if input_list[i]== input_list[i+1]+1 or input_list[i]== input_list[i+1]-1:
            count+=1
            if count>temp:
                temp=count
        else :
            count=0
    return (temp+1)

if __name__=="__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))