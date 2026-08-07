# WRITE YOUR SOLUTION HERE:
def recursive_sum(num: int):

    if num<=1:
        return 1

    return num + recursive_sum(num-1)

if __name__=="__main__":
    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))