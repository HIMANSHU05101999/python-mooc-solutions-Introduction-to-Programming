# Write your solution here:
class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour=hour
        self.minute=minute
        self.second=second

    def tick(self):
        self.second+=1
        if self.second==60:
            self.minute+=1
            self.second=0
        if self.minute==60:
            self.hour+=1
            self.minute=0
        if self.hour==24:
            self.hour=0

    def set(self, hours: int, minutes: int):
        self.hour=hours
        self.minute=minutes
        self.second=0



    def __str__(self):
        return (f"{self.hour:02}:{self.minute:02}:{self.second:02}")
    
def main():
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)

if __name__=="__main__":
    main()