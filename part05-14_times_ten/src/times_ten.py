# Write your solution here
def times_ten(start_index: int, end_index: int):
    dic={}
    for i in range (start_index,end_index+1):
        dic[i]=i*10

    return dic

def main():
    d = times_ten(3, 6)
    print(d)

if __name__=="__main__":
    main()