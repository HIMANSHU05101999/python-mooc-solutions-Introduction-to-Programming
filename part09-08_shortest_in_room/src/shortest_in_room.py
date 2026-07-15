# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people=[]

    def is_empty(self):
        if self.people:
            return False
        return True

    def add(self, person: Person):
        self.people.append(person)

    def print_contents(self):
        total_height=0
        name_height_list=""
        for item in self.people:
            total_height+=item.height
            name_height_list+=(f" {item.name} ({item.height} cm)\n")
        print(f"There are {len(self.people)} persons in the room, and their combined height is {total_height} cm\n{name_height_list}")

    def shortest(self):
        if self.people:
            shortest=self.people[0].height
            ret_obj=0
            for item in self.people:
                if shortest>=item.height:
                    shortest=item.height
                    ret_obj=item
            return ret_obj
        return None

    def remove_shortest_my(self):
        if self.people:
            shortest=self.people[0].height
            name=""
            index=0
            for item in self.people:
                if shortest>=item.height:
                    shortest=item.height
                    name=item.name
                    rmv=item
                    index=self.people.index(item)
            self.people.pop(index)        
            return rmv
        return None

    def remove_shortest(self):
        shortest=self.shortest()
        if shortest:
            self.people.remove(shortest)
        return shortest
        


def main():
    room = Room()

    #room.add(Person("Lea", 183))
    #room.add(Person("Kenya", 172))
    #room.add(Person("Nina", 162))
    #room.add(Person("Ally", 166))
    #room.add(Person("Ann",120))
    #room.add(Person("Tim",150))
    room.add(Person("Grace",180))
    room.add(Person("Jan",175))
    room.add(Person("Lisa",150))
    room.add(Person("Paul",204))
    room.add(Person("Jana",171))
    room.add(Person("Ruth",149))
    
    room.print_contents()
    print(room.shortest())
    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
if __name__=="__main__":
    main()