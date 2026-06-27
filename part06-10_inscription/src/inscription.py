# Write your solution here
def main():

    string=input("Whom should I sign this to:")
    file_name=input("Where shall I save it:")
    write_this=f"Hi {string}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
    with open(file_name,"w") as file:
        file.write(write_this)

#if __name__=="__main__":
main()    
    