# Write your solution here
def anagrams(str1,str2):
    sortedstr1=sorted(str1)
    sortedstr2=sorted(str2)
    if sortedstr1==sortedstr2:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(anagrams("abc","cba"))
