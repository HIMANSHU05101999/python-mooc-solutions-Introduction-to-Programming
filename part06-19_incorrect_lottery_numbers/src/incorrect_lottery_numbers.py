# Write your solution here
def split_numbers(line: str):
    new_line=line.strip().split(";")
    number_split=(new_line[1].split(","))
    return(number_split)

def check_week(line: str):
    new_line=line.strip().split(";")
    week_split=(new_line[0].split(" "))
    try:
        int(week_split[1])
        return(line)        
    except ValueError:
        pass
    return(f"The week number is incorrect: {line}")

def numbers_incorrect(line: str):
        number_split=split_numbers(line)
        for item in number_split:
            try:
                int(item)
            except ValueError:
                return(f"One or more numbers are not correct: {line}")
        return(line)

def len_check(line: str):
        number_split=split_numbers(line)
        length_of_lottery_string=len(number_split)
        if length_of_lottery_string==7:
            return(line)
        else:
            return(f"Too few numbers: {line}")

def size_check(line: str):
    number_split=split_numbers(line)
    for item in number_split:
        try:
            val=int(item)
            if val<0 or val>40:
                return(f"The numbers are too small or large: {line}")     
        except ValueError:
            pass
    return(line)   
        
def check_twice(line: str):
    number_split=split_numbers(line)
    test_list=[]
    for item in number_split:
        try:
            val=int(item)
            if val in test_list:
                return(f"The same number appears twice: {line}")
            test_list.append(val)
        except ValueError:
            pass
    return(line)   

def filter_incorrect():
    with open("correct_numbers.csv","w") as correct_file:
        pass
    from pathlib import Path
    file_name=Path(__file__).parent/"lottery_numbers.csv"
    with open("correct_numbers.csv","a") as correct_file:
        with open(file_name) as file:
            for line in file:
                if check_week(line)==line:
                    if numbers_incorrect(line)==line:
                        if len_check(line)==line:
                            if size_check(line)==line:
                                if check_twice(line)==line:
                                    print(line)
                                    correct_file.write(line)

def main():
    filter_incorrect()
if __name__=="__main__":
    main()

