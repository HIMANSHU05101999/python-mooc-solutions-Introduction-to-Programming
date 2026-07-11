# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.list_of_number=[]
        self.temp=[]

    def add_number(self, number:int):
        self.list_of_number.append(number)

    def count_numbers(self):
        return len(self.list_of_number)
    
    def get_sum(self):
        return sum(self.list_of_number)

    def average(self):
        if (self.list_of_number):
            return sum(self.list_of_number)/len(self.list_of_number)
        else:
            return 0
    
    #def sum_of_even(self):
        self.temp=[]
        for num in self.list_of_number:
            if num%2==0:
                self.temp.append(num)
        return sum(self.temp)
    
    #def sum_of_odd(self):
        self.temp=[]
        for num in self.list_of_number:
            if num%2!=0:
                self.temp.append(num)
        return sum(self.temp)
    

def main():
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())

def main1():
    print("Please type in integer numbers:")
    stats = NumberStats()
    odd = NumberStats()
    even = NumberStats()
    while True:
        num=int(input())
        if num<0:
            break
        stats.add_number(num)
        if num%2==0:
            even.add_number(num)
        else:
            odd.add_number(num)
    print(f"Sum of numbers: {stats.get_sum()} \nMean of numbers: {stats.average()} \nSum of even numbers: {even.get_sum()} \nSum of odd numbers: {odd.get_sum()}")    

#main()
main1()