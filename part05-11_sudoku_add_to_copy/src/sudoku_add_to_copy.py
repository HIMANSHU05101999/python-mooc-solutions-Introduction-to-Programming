# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku=[]
    new_row=[]
    for r in range (len(sudoku)):
        for c in range (len(sudoku[r])):
    
            new_row.append(sudoku[r][c])
        new_sudoku.append(new_row)
        new_row=[]
    new_sudoku[row_no][column_no]=number
    return new_sudoku

def print_sudoku(sudoku: list):

    for r in range (len(sudoku)):
        for c in range (len(sudoku[r])):
            if sudoku[r][c]!=0:
                print(f"{sudoku[r][c] }",end="")
            else:
                print("_ ",end="")
            if (c+1)%3==0:
                print(" ",end="")
        if (r+1)%3==0:
            print()   
        print()    




if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

