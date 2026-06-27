# Write your solution here
def chessboard(num):
    row=0
    while row<num:
        row+=1
        col=0
        line=""
        while col<num:
            col+=1
            if (row+col)%2==0:
                line+="1"
            else:
                line+="0"
        print(line)

            


# Testing the function
if __name__ == "__main__":
    chessboard(3)
