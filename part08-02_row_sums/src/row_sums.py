# Write your solution 
def row_sums(matrix: list):
    
    for row in matrix:
        total=0
        for num in row:
            total+=num
        row.append(total)

def main():
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
if __name__=='__main__':
    main()