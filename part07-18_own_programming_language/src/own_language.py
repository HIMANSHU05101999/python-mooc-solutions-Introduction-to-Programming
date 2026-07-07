# Write your solution here

    
def add(a: int, b: int):
    return a+b

def sub(a: int, b: int):
    return a-b
    
def mul(a: int, b: int):
    return a*b
    


def run(program: list):
    assign_dict={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
    var_dict=assign_dict
    result=[]
    for item in program:
        items=item.strip().split(" ")
        if items[0]=="MOV":
            try:    
                var_dict[items[1]]=int(items[2])
            except ValueError:
                var_dict[items[1]]=var_dict[items[2]]
        elif items[0]=="PRINT":
            if items[1] in var_dict:
                result.append(var_dict[items[1]])
        elif items[0]=="ADD":
            try:
                addition=add(var_dict[items[1]],var_dict[items[2]])
            except KeyError:
                addition=sub(var_dict[items[1]],int(items[2]))
            var_dict[items[1]]=addition
        elif items[0]=="SUB":
            try:
                substraction=sub(var_dict[items[1]],var_dict[items[2]])
            except KeyError:
                substraction=sub(var_dict[items[1]],int(items[2]))
            var_dict[items[1]]=substraction
        elif items[0]=="MUL":
            try:
                multply=mul(var_dict[items[1]],var_dict[items[2]])
            except KeyError:
                multply=mul(var_dict[items[1]],int(items[2]))
            var_dict[items[1]]=multply
        elif items[0]=="END":
            return result
        else:
            return result
    return result

def main():
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
if __name__=="__main__":
    main()



