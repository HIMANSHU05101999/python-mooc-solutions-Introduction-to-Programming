# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    
    def bigger(self, compare_size: "RealProperty"):
        return self.square_metres>compare_size.square_metres
    
    def price_difference(self, compare_diff: "RealProperty"):
        p1=self.square_metres*self.price_per_sqm
        p2=compare_diff.square_metres*compare_diff.price_per_sqm
        return abs(p1-p2)
    
    def more_expensive(self, compare_price: "RealProperty"):
        p1=self.square_metres*self.price_per_sqm
        p2=compare_price.square_metres*compare_price.price_per_sqm
        return p1>p2

def main():
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))
    print()
    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))
    print()
    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))

if __name__=="__main__":
    main()