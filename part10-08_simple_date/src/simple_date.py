# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date=date
        self.__month=month
        self.__year=year

    def __lt__(self, another : "SimpleDate"):
        return not self.__gt__(another)
        

    def __gt__(self, another : "SimpleDate"):
        if self.__year>another.__year:
            return True
        elif self.__year==another.__year:
            if self.__month>another.__month:
                return True
            elif self.__month==another.__month:
                if self.__date>another.__date:
                    return True
                else:
                    return False
            else:
                return False
        else: 
            return False

    def __eq__(self, another: "SimpleDate"):
        if self.__year==another.__year:
            if self.__month==another.__month:
                if self.__date==another.__date:
                    return True
                else:
                    return False
            else:
                return False
        else:
                return False

    def __ne__(self, another):
        return not self.__eq__(another)

    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"

    

def main():
    d1 = SimpleDate(4, 10, 2020)
    #d2 = SimpleDate(28, 12, 1985)
    #d3 = SimpleDate(28, 12, 1985)

    #print(d1)
    #print(d2)
    #print(d1 == d2)
    #print(d1 != d2)
    #print(d1 == d3)
    #print(d1 < d2)
    #print(d1 > d2)
    #print(d1+400)
if __name__=="__main__":
    main()

