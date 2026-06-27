# Write your solution here
def sudoku_grid_row_check(sudoku: list):
    row=[]
    #print("Row Check")
    for r in range (0,9):
        for i in range (0,9):
            if sudoku[r][i]>0 and sudoku[r][i] in row:
                #print(round)
                #print(False)
                return False
            row.append(sudoku[r][i])
        #print(row)     
        #print(True) 
        row=[]
    return True

def sudoku_grid_column_check(sudoku: list):   
    column=[]
    update=[]
    #print("Column Check")
    
    for inc in range (0,9):
        for row in range (0,9):
            column.append(sudoku[row][inc])
       
        for i in range(0,9):
            if column[i]>0 and column[i] in update:
                #print(update)
                #print(False)
                return False
            update.append(column[i])
        #print(update)
        #print(True)
        update=[]
        column=[]  
    return True

def sudoku_grid_grid_check(sudoku: list):
    indexes=[(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    row=[]
    update=[]
    for item in indexes:
        for i in range (item[0],item[0]+3):
            for j in range (item[1],item[1]+3):
                row.append(sudoku[i][j])
        #print(row)
        #row=[]
        for i in range(0,9):
            if row[i]>0 and row[i] in update:
                #print(update)
                #print(False)
                return False
            update.append(row[i])
        #print(update)
        #print(True)
        update=[]
        row=[]  
    return True


def sudoku_grid_correct(sudoku: list):
    
    if sudoku_grid_row_check(sudoku)==True:
        if sudoku_grid_column_check(sudoku)==True:
            if sudoku_grid_grid_check(sudoku)==True:
                return True
    return False




    
if __name__=="__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))