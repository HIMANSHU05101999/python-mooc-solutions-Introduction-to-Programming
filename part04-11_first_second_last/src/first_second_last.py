# Write your solution here
def check(string,target):
    index=0
    count=1
    first_index=0
    word=[]
    while index < len(string):
            if string[index] == " ":
                word.append(string[first_index:index])          
                if count==target:
                    return word[target-1]
                first_index=index+1
                count+=1
            index+=1

        
def first_word(string):
    return check(string,1)
    
def second_word(string):
    if check(string,2)!=None:
        return check(string,2)
    else:
        index=0
        while index<len(string):
            index+=1
            if string[-index]==" ":
                return string[-index+1:]

def last_word(string):
    index=0
    while index<len(string):
         index+=1
         if string[-index]==" ":
              return string[-index+1:]
         
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    

