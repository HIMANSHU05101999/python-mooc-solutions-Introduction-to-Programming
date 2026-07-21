# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    
    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another):
        if self.__euros==another.__euros and self.__cents==another.__cents:
            return True
        return False

    def __lt__(self, another):
        if self.__euros<another.__euros:
            return True
        elif self.__euros==another.__euros and self.__cents<another.__cents:
            return True
        return False

    def __gt__(self, another):
        if self.__euros>another.__euros:
            return True
        elif self.__euros==another.__euros and self.__cents>another.__cents:
            return True
        return False

    def __ne__(self, another):
        if self.__euros!=another.__euros:
            return True
        elif self.__euros==another.__euros and self.__cents!=another.__cents:
            return True
        return False
    
    def __add__(self, another):
        m1=(self.__euros*100)+self.__cents
        m2=(another.__euros*100)+another.__cents
        total=m1+m2
        euro=total//100
        cent=total%100
        return Money(euro,cent)

    def __sub__(self, another):
        m1=(self.__euros*100)+self.__cents
        m2=(another.__euros*100)+another.__cents
        total=m1-m2
        euro=total//100
        cent=total%100
        if total<0:
            raise ValueError
        return Money(euro,cent)
        

def main():
    e1 = Money(1, 0)
    e2 = Money(2, 0)  # two euros and five cents
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e1-e2

    print(e5)

    print(e1)
    e1.euros = 1000
    print(e1)
if __name__=="__main__":
    main()




