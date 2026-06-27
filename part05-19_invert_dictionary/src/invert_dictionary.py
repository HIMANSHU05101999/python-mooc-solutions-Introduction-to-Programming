# Write your solution here
def invert_MySol(dictionary: dict):
    new_dict={}
    for key in dictionary:
        new_dict[dictionary[key]]=key
    dictionary.clear()
    for key in new_dict:
        dictionary[key]=new_dict[key]

def invert(dictionary: dict):
    new_dict={}
    for key in dictionary:
        new_dict[key]=dictionary[key]
    for key in new_dict:
        del dictionary[key]
    for key in new_dict:
        dictionary[new_dict[key]]=key 

def main():
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

if __name__=="__main__":
    main()