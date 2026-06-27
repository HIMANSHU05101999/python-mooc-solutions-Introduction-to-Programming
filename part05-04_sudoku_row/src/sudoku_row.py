# Write your solution here
def row_correct_MySol(sudoku: list, row_no: int):
    check_list=[1,2,3,4,5,6,7,8,9]
    count_list=[0]*9
    row=sudoku[row_no]
    for item in row:
        #for num in check_list:
        #        if num==item:
        #            count_list[num-1]+=1
        if item!=0:
            count_list[item-1]+=1

    for item in count_list:
        if item>=2:
              return False
    return True

def row_correct(sudoku: list, row_no: int):
    nums=[]
    for num in sudoku[row_no]:
        if num>0 and num in nums:
            return False
        nums.append(num)
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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))