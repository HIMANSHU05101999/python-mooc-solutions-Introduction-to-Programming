# Write your solution here
def spruce(num):
    print("a spruce!")
    stars=1
    spaces=num
    while spaces>0:
        print(((spaces-1)*" "+stars*"*"))
        spaces-=1
        stars+=2
    print((num-1)*" "+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(10)