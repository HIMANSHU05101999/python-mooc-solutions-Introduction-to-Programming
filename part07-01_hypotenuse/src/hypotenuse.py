# Write your solution here
from math import sqrt

def hypotenuse(leg1: float, leg2: float):
    return sqrt(leg1**2 + leg2**2)

def main():
    print(hypotenuse(1,2))
if __name__=="__main__":
    main()