# Write your solution here
def print_sudoku_structur(sudoku: list):
    for row in range(0,len(sudoku)):
        for col in range(0,len(sudoku[row])):
            if col==2 or col==5:
                print("_ ",end="")
            else: 
                print("_",end="")
        if row==2 or row==5:
            print("\n")
        else:
            print("")    

def print_sudoku(sudoku: list):
    for row in range(0,len(sudoku)):
        for col in range(0,len(sudoku[row])):  
                if sudoku[row][col]!=0:
                    print(f"{sudoku[row][col]} ",end="")
                else:
                    print("_ ",end="")
                if col==2 or col==5:
                    print(" ",end="") 
        if row==2 or row==5:
            print()        
        print()
            
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no]=number
    
    
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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)