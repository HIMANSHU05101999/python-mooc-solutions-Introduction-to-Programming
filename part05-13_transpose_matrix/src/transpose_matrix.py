# Write your solution here

def transpose(matrix: list):
    row=[]
    update_matrix=[]
    for l in range (len(matrix)):
        for il in range (len(matrix[l])):
            row.append(matrix[il][l])
        update_matrix.append(row)
        row=[]    
        print()
    matrix[:]=update_matrix
    #return (matrix)
if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(matrix))