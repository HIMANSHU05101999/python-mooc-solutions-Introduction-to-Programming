# Copy here code of line function from previous exercise
def line(size,char):
    if char=="":
        print("*"*size)
    else:
        print(char[0]*size)
        
def square_of_hashes(size):
    i=0
    while i<size:
        i+=1
# You should call function line here with proper parameters
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    