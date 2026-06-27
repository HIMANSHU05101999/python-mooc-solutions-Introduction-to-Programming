# Write your solution here
def palindromes(string):
    reversed=""
    for i in range(len(string)-1,-1,-1):
        reversed+=string[i]
    if string==reversed:
        return True
    else:
        return False
# Note, that at this time the main program should not be written inside
#if __name__ == "__main__":
string="abc"
while palindromes(string)==False:
    string = input("Please type in a palindrome:")
    if palindromes(string)==True:
        print(f"{string} is a palindrome!")
    else:
        print("that wasn't a palindrome")
          