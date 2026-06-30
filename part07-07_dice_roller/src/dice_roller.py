# Write your solution here
import random
def roll(die: str):
    dice={
    "A":(3,3,3,3,3,6),
    "B":(2,2,2,5,5,5),
    "C":(1,4,4,4,4,4)
    }
    return random.choice(dice[die])

def play(die1: str, die2: str, times: int):
    die1win=0
    die2win=0
    draw=0
    for i in range(times):
        die1roll=roll(die1)
        die2roll=roll(die2)
        if die1roll>die2roll:
            die1win+=1
        elif die1roll<die2roll:
            die2win+=1
        elif die1roll==die2roll:
            draw+=1
    return(die1win,die2win,draw)

def main():

    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("C", "A", 5)
    print(result)
    result = play("A", "B", 5)
    print(result)

if __name__=="__main__":
    main()