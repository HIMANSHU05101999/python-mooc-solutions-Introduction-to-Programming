# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        if name!="":
            self.__name=name
        else: 
            raise ValueError ("Name can not be empty")

        if weight>0:
            self.__weight=weight
        else:
            raise ValueError ("Weight can not be 0 or negative")

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return (f"{self.__name} ({self.__weight} kg)")
    

class Suitcase:
    def __init__(self, max_weight: int):
        if max_weight>0:
            self.__max_weight=max_weight
        else:
            raise ValueError ("Max Weight limit can not be 0 or negative")

        self.__items_in_suitcase=[]

    def add_item(self, item_rcv):
        total_weight=self.weight()
        
        if self.__max_weight >= total_weight + item_rcv.weight():
            self.__items_in_suitcase.append(item_rcv)
        
    def __str__(self):
        total_items=len(self.__items_in_suitcase)
        total_weight=self.weight()

        if total_items==1:
            return (f"{total_items} item ({total_weight} kg)")
        return (f"{total_items} items ({total_weight} kg)")

    def print_items(self):
        for item in self.__items_in_suitcase:
            print(item)
    
    def weight(self):
        total_weight=0
        for item in self.__items_in_suitcase:
            total_weight+=item.weight()
        return total_weight

    def heaviest_item(self):
        if self.__items_in_suitcase:
            heaviest=self.__items_in_suitcase[0]    
            for item in self.__items_in_suitcase:
                if heaviest.weight()<=item.weight():
                    heaviest=item
            return heaviest
        return None
    
class CargoHold:
    def __init__(self, max_weight: int):
        if max_weight>0:
            self.__max_weight=max_weight
        else:
            raise ValueError ("Max Weight limit can not be 0 or negative") 
        
        self.__total_suitcase=[]
    
    def add_suitcase(self, itm_rvc):
        total_weight=self.total_weight()
        if self.__max_weight >= total_weight + itm_rvc.weight():
            self.__total_suitcase.append(itm_rvc)
        
    def __str__(self):
        total_weight=self.total_weight()
        total_items=len(self.__total_suitcase)
        limit_left=self.__max_weight-total_weight
        if total_items==1:
            return (f"{total_items} suitcase, space for {limit_left} kg")
        return (f"{total_items} suitcases, space for {limit_left} kg")

    def print_items(self):
        for item in self.__total_suitcase:
            item.print_items()

    def total_weight(self):
        total_weight=0
        for item in self.__total_suitcase:
            total_weight+=item.weight()
        return total_weight
        

def main():
    #book = Item("ABC Book", 2)
    #phone = Item("Nokia 3210", 1)
    #brick = Item("Brick", 4)

    #suitcase = Suitcase(10)
    #suitcase.add_item(book)
    #suitcase.add_item(phone)
    #suitcase.add_item(brick)
    suitcase = Suitcase(25)
    item1 = Item("ABC Book", 2)
    suitcase.add_item(item1)
    item2 = Item("Hammer", 10)
    suitcase.add_item(item2)
    item3 = Item("Rock", 3)
    suitcase.add_item(item3)
    heaviest=suitcase.heaviest_item()
    #heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

if __name__=="__main__":
    main()
