# Write your solution here
import csv
from pathlib import Path
from datetime import datetime
def cheaters():
    start_dict={}
    cheater_list=[]
    start_time_file=Path(__file__).parent/"start_times.csv"
    submission_file=Path(__file__).parent/"submissions.csv"
    with open(start_time_file) as start_file, open(submission_file) as sub_file:
        for line in csv.reader(start_file,delimiter=";"):
           start_dict[line[0]]=datetime.strptime(line[1],'%H:%M')
        for line in csv.reader(sub_file,delimiter=";"):
            print(line)
   
        for key,val in start_dict.items():
            if key in line:
                if datetime.strptime(line[3],'%H:%M')-val>3:
                    cheater_list.append(key)
        print(cheater_list)


            
                    

   
       
def main():
    cheaters()
if __name__=="__main__":
    main()