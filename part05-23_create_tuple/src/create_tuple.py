# Write your solution here
def create_tuple(x: int, y: int, z: int):
    return(smallest(x,y,z),
    greatest(x,y,z),
    add(x,y,z))
def greatest(x: int, y: int, z: int):
    if x>y and x>z:
        return(x)
    elif y>z and y>x :
        return(y)
    else:
        return(z)

def smallest(x: int, y: int, z: int):
    if x<y and x<z:
        return(x)
    elif y<z and y<x:
        return(y)
    else:
        return(z)

def add(x: int, y: int, z: int):
    return(x+y+z)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))