# Write your solution here
def filter_solutions():
    with open("correct.csv","w") as file:
        pass
    with open("incorrect.csv","w") as file:
        pass
    with open("solutions.csv") as file:
        for line in file:
            new_line=(line.strip().split(";"))
            for i in range(len(new_line[1])):
                    if new_line[1][i]=="+" or new_line[1][i]=="-":
                        num1=int(new_line[1][0:i])
                        num2=int(new_line[1][i+1:])
                        operator=new_line[1][i]
                        result=int(new_line[2])
                        if operator=="+":
                            if num1+num2==result:
                                correct(line)
                            else:
                                incorrect(line)
                        elif operator=="-":
                            if num1-num2==result:
                                correct(line)
                            else:
                                incorrect(line)


def correct(correct_input: str):
    with open("correct.csv","a") as file:
        file.write(correct_input)

def incorrect(incorrect_input: str):
    with open("incorrect.csv","a") as file:
        file.write(incorrect_input)


def main():
    filter_solutions()
if __name__=="__main__":  
    main()
