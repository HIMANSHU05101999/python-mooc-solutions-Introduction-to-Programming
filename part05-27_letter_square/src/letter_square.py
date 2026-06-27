# Write your solution here
def square(layers: int):
    size=(2*layers)-1
    r=0
    c=0
    for r in range(size):
        for c in range (size):
                layer_num=(min(r,c,size-1-r,size-1-c))
                print(f"{chr(65+layers-1-layer_num)}",end="")   
        print()
    
def main():
    layer=int(input("Layers"))
    (square(layer))
main()