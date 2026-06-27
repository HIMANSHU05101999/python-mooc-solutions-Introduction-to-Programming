# Write your solution here
def line(num,char):
    i=0
    while i<num:
        i+=1
        if char=="":
            char="*"
        elif len(char)>1:
            char=char[0]
        print(char,end="")

    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")