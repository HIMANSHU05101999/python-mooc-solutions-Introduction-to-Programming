# Write your solution here

def find_words(search_item: str):       
    from pathlib import Path
    file_name=Path(__file__).parent/"words.txt"
    word_list=[]
    with open(file_name) as file:
        for line in file:
            new_line=line.strip()
            if "*" in search_item:
                for i in range (len(search_item)):
                    if search_item[i]=="*":
                        if i==0:
                            if (new_line.endswith(search_item[1:]))==True:
                                word_list.append(new_line)
                        elif i==len(search_item)-1:
                            if (new_line.startswith(search_item[:-1]))==True:
                                word_list.append(new_line)
            elif "." in search_item:                
                if len(new_line)==len(search_item):
                    for i in range(len(new_line)):
                        if new_line[i]!=search_item[i] and search_item[i]!=".":
                            check=False
                            break
                        else:
                            check=True
                    if check==True:
                        word_list.append(new_line)
            else:
                if search_item == new_line:
                    word_list.append(new_line)
    return(word_list)

def main():
    print(find_words("c..e"))
if __name__=="__main__":
    main()