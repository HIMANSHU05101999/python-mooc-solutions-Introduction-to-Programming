# Write your solution here
word=input("Please type in a string:")
char=input("Please type in a substring:")
#word="abababa"
#char="aba"
a=word.find(char)
part_string1=word[0:a+len(char)]
part_string2=word[a+len(char):]
b=part_string2.find(char)
#print(b+len(part_string1))
#print(part_string1)
#print(part_string2)
if char in part_string2:
    print(f"The second occurrence of the substring is at index {b+len(part_string1)}.")
else:
    print("The substring does not occur twice in the string.")