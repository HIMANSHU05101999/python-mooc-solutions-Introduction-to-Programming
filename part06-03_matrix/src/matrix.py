# write your solution here
def matrix_sum():
    from pathlib import Path
    file_path=Path(__file__).parent /"matrix.txt"
    sum=0
    with open(file_path) as file:
        for item in file:
            new=item.split(",")
            for string in new:
                num=int(string)
                sum+=num
    return(sum)
    
    
def matrix_max():
    from pathlib import Path
    file_path=Path(__file__).parent /"matrix.txt"
    temp=0
    with open(file_path) as file:
        for item in file:
            new=item.split(",")
            for string in new:
                num=int(string)
                if temp<num:
                    temp=num
    return(temp)
    
def row_sums():
    from pathlib import Path
    file_path=Path(__file__).parent /"matrix.txt"
    sum_list=[]
    with open(file_path) as file:
        for item in file:
            new=item.split(",")
            sum=0
            for string in new:
                num=int(string)
                sum+=num
            sum_list.append(sum)
    return(sum_list)

                


def main():
    print(matrix_sum())
    print(matrix_max())   
    print(row_sums())     

if __name__=="__main__":
 main()