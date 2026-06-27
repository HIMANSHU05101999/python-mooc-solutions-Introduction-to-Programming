# write your solution here
def largest():
    from pathlib import Path
    file_path = Path(__file__).parent / "numbers.txt"
    temp=0
    with open("numbers.txt") as num_file:
        for number in num_file:
            number=int(number)
            if temp<number:
                temp=number
            return(temp)


def main():
    print(largest())

if __name__=="__main__":   
    main()

