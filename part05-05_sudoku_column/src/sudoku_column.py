# Write your solution here
def column_correct(sudoku: list, column_no: int):
    coulumn=[]
    update=[]
    for i in range (0,len(sudoku)):
        for j in range(0,len(sudoku[i])):
            if j==column_no:
                coulumn.append(sudoku[i][j])
    
    print(coulumn)
    for item in coulumn:
        if item>0 and item in update:
            return False
        update.append(item)
    return True
    
if __name__=="__main__":
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))