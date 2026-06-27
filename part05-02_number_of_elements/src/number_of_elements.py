# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count=0
    for i in range(0,len(my_matrix)):
        for j in range(0,len(my_matrix[i])):
            if my_matrix[i][j]==element:
                count+=1
    return (count)

if __name__=="__main__":
    m = [[5, 1, 3, 1, 5], [1, 2, 4, 5, 5], [4, 4, 4, 5, 5], [2, 5, 1, 4, 5], [3, 5, 2, 4, 5]]
    print(count_matching_elements(m, 5))