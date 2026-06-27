# Write your solution here
def read_input(string: str, lower_limit: int, upper_limit: int):
    while True:
        try:
            user_input=int(input(string))
            if user_input>lower_limit and user_input<upper_limit:
                return(user_input)
        
        except ValueError:
            pass
        
        print(f"You must type in an integer between {lower_limit} and {upper_limit}")

def main():
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
if __name__=="__main__":

    main()