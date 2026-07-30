# WRITE YOUR SOLUTION HERE:
def rows_of_stars(numbers: list):
    return [number * "*" for number in numbers]

if __name__=="__main__":
    l=[1,2,3,4,5]
    new_l=(rows_of_stars(l))
    [print(item) for item in new_l]