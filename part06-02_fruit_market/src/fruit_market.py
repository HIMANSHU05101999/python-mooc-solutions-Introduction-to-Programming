# write your solution here
def read_fruits():

    from pathlib import Path
    file_path = Path(__file__).parent / "fruits.csv"
    dictionary={}

    with open(file_path) as file:
    
        for item in file:
            part=(item.split(";"))
            part[1]=float(part[1].replace("\n",""))
            dictionary[part[0]]=part[1]
    return(dictionary)
def main():
    print(read_fruits())
if __name__=="__main__":
    main()
