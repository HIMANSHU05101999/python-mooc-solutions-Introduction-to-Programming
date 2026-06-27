#Testing the functions
string="once upon a time there was a programmer"
index=0
count=1
first_index=0
word=""
target=count
while index < len(string):
        if string[index] == " ":
            word=string[first_index:index]
            #print(f"Letter: {string[index+1]} Word Count: {count+1} First Index: {first_index} Last Index: {index-1} Word: {word}")
            print(f"{count} Word: {string[first_index:index]}")
            first_index=index+1
            count+=1
        index+=1
        
print(f"{count} Word: {string[first_index:]}")
#print(type(word))
#print(word)


# Find the position of the string
# Write your solution here
def check(string,target):
    index=0
    count=1
    first_index=0
    word=[]
    while index < len(string):
            if string[index] == " ":
                word.append(string[first_index:index])
                #print(f"Letter: {string[index+1]} Word Count: {count+1} First Index: {first_index} Last Index: {index-1} Word: {word}")
                #print(f"{count} Word: {string[first_index:index]}")
                
                if count==target:
                    return word[target]
                
                first_index=index+1
                count+=1
            index+=1
    #print(f"{count} Word: {string[first_index:]}")
        
    
        
def first_word(string):
    return check(string,1)
    
def second_word(string):
    return check(string,2)

def last_word(string):
    index=0
    while index<len(string):
         index+=1
         if string[-index]==" ":
              return string[-index+1:]
         
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
        

