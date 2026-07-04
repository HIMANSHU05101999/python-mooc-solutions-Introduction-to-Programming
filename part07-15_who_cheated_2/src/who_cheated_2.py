# Write your solution here
from pathlib import Path
from datetime import datetime,timedelta
import csv
def final_points():
    start_dict={}
    stud_score={}
    start_file=Path(__file__).parent/"start_times.csv"
    sub_file=Path(__file__).parent/"submissions.csv"
    with open(start_file) as start, open(sub_file) as sub:
        for line in csv.reader(start,delimiter=";"):
            name=line[0]
            time=datetime.strptime(line[1],'%H:%M')
            start_dict[name]=time
    #print(start_dict)
        for line in csv.reader(sub,delimiter=";"):
            name=line[0]
            task=line[1]
            point=int(line[2])
            start_time=start_dict[name]
            sub_time=datetime.strptime(line[3],'%H:%M')
            if sub_time-start_time<=timedelta(hours=3):
                #print(name,task,point)
                if name not in stud_score:
                    stud_score[name]={}
                
                if task not in stud_score[name]:
                    stud_score[name][task]=point
                else:
                    if point>stud_score[name][task]:
                        stud_score[name][task]=point
    #print(stud_score)
    new_dict={}           
    for name,scores in stud_score.items():
        #print(name,scores)
        total=0
        for tasks,score in scores.items():
            #print(tasks,score)
            total+=scores[tasks]
            new_dict[name]=total
    return (new_dict)

def main():
    final_points()
if __name__=="__main__":
    main()