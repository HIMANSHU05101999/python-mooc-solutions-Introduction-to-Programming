# Write your solution here
def no_vowels_without_replace(input_string):
    vowels="aeiou"
    for i in range (0,len(vowels)):
        new_string=""
        for j in range (0,len(input_string)):
            if vowels[i]!=input_string[j]:
                new_string+=input_string[j]
        input_string=new_string
    return (new_string)


def no_vowels(input_string):
    vowels="aeiou"
    new_string=""
    for i in vowels:
        new_string=input_string.replace(i,"")
        input_string=new_string
    return new_string

if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

    
