# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.first_value=initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value>0:
            self.value-=1
        else:
            self.value=0
    # Write the rest of the methods here!
    def set_to_zero(self):
        self.value=0

    def reset_original_value(self):
        self.value=self.first_value

def main():
    counter = DecreasingCounter(10)
    counter.print_value()
    counter.decrease() 
    counter.print_value()
    counter.decrease()
    counter.print_value()
if __name__=="__main__":
    main()