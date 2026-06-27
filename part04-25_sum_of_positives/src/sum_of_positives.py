# Write your solution here
def sum_of_positives(input_list):
    sum=0
    for i in range (0,len(input_list)):
        if input_list[i]>0:
            sum+=input_list[i]
    return sum
if __name__=="__main__":
    my_list = [-9, -7, -5, -2, 0, 1, 3, 5, 7, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)