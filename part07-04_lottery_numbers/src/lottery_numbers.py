# Write your solution here
import random
def lottery_numbers(amount: int, lower: int, upper: int):
    lot_list=[]
    i=0
    while i<amount:
        lot_num=random.randint(lower,upper)
        if lot_num not in lot_list:
            lot_list.append(lot_num)
        elif lot_num in lot_list:
            i=i-1
        i+=1
    sort_list=sorted(lot_list)
    return(sort_list)

def main():
    print(lottery_numbers(3,2,22))
if __name__=="__main__":
    main()