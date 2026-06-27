# Copy here code of line function from previous exercise
def line(num,char):
    if char=="":
        print("*"*num)
    else:
        print(char[0]*num)

def triangle(size):
    i=0
    while i<1:
        i+=1
        j=0
        while j<size:
            j+=1
    # You should call function line here with proper parameters
            line(j, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
