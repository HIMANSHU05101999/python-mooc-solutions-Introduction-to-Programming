# Write your solution here
import fractions
def fractionate(amount: int):
    ret_list=[]
    for i in range(amount):
        fract=fractions.Fraction(1,amount)
        ret_list.append(fract)
    return (ret_list)


def main():
    for p in fractionate(3):
        print(p)
    print()
    print(fractionate(5))

if __name__=="__main__":
    main()
