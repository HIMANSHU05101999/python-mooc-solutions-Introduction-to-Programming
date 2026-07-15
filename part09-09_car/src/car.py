# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__fuel=0
        self.__drive=0
    
    def fill_up(self):
        self.__fuel=60

    def drive(self, km_drive: int):
        if self.__fuel>=km_drive:
            self.__fuel -= km_drive
            self.__drive += km_drive
        else:
            self.__drive+=self.__fuel
            self.__fuel=0
        




    def __str__(self):
        return (f"Car: odometer reading {self.__drive} km, petrol remaining {self.__fuel} litres")
            
    
def main():
    car = Car()
    #print(car)
    car.fill_up()
    #print(car)
    #car.drive(20)
    #print(car)
    #car.drive(50)
    #print(car)
    #car.drive(10)
    #print(car)
    #car.fill_up()
    #car.fill_up()
    car.drive(10)
    car.drive(20)
    car.drive(10)
    car.drive(20)
    print(car)
if __name__=="__main__":
    main()
