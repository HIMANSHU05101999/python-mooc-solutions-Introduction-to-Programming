# Write your solution here
import json
def print_persons(filename: str):
    from pathlib import Path
    file_name=Path(__file__).parent/filename
    with open(file_name) as file:
        data=file.read()
    person=json.loads(data)
    
    new_str=""
    for item in person:
        for key,val in item.items():
            if key=="name":
                new_str+=val+" "
            if key=="age":
                val=str(val)+" years "
                new_str+=val
            if key=="hobbies":
                if val!=[]:
                    string=""
                    for i in range(len(val)):
                        if i==0:
                            string+=str('(') 
                        if i<len(val)-1:
                            string+=str(val[i]+', ')    
                        else:
                            string+=str(val[i]+')\n')
                    val=string  
                    string=""
                    new_str+=val
                else:
                    new_str=new_str+"()\n"
    print(new_str[:-1])


def main():
    print_persons("file4.json")
if __name__=="__main__":
    main()