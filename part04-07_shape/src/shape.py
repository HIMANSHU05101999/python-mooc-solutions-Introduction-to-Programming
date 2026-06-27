# Copy here code of line function from previous exercise and use it in your solution
def line(num,char):
    if char=="":
        print("*"*num)
    else:
        print(char[0]*num)

def shape(tri_num,tri_char,rect_num,rect_char):
    i=0
    while i<1:
        i+=1
        j=0
        while j<tri_num:
            j+=1
            line(j,tri_char)
        k=0
        while k<rect_num:
            k+=1
            line(tri_num,rect_char)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 4, "o")