# tee ratkaisu tänne
from pathlib import Path
import csv
def course_grading_3():
    
    student_file=input("Student information:")
    exercise_file=input("Exercises completed:")
    exam_point_file=input("Exam points:")
    
    stud_dict={}
    exer_dict={}
    exam_dict={}
    with open(student_file) as studfile, open(exercise_file) as exerfile, open(exam_point_file) as examfile:
        for line in csv.reader(studfile):
            line=line[0].strip().split(";")
            if line[0]=='id':
                continue
            stud_dict[line[0]]=f"{line[1]} {line[2]}"
        #print(stud_dict)
        for line in csv.reader(exerfile):
            line=line[0].strip().split(";")
            exerscore=[]
            if line[0]=='id':
                continue
            for item in line:
                if len(item)>2:
                    continue
                else:
                    exerscore.append(int(item))
            #print(exerscore)        
            exer_dict[line[0]]=exerscore
            exer_dict[f"{'Exercise_Total'} {line[0]}"]=sum(exerscore)
            exer_dict[f"{'Exercise_Point'} {line[0]}"]=sum(exerscore)//4
        #print(exer_dict)
        for line in csv.reader(examfile):
            line=line[0].strip().split(";")
            exampoint=[]
            if line[0]=='id':
                continue
            for item in line:
                if len(item)>2:
                    continue
                else:
                    exampoint.append(int(item))
            exam_dict[line[0]]=exampoint
            exam_dict[f"{'Exam_Total'} {line[0]}"]=sum(exampoint)
        #print(exam_dict)
    grade_point_dict={0:[0,14],
                      1:[15,17],
                      2:[18,20],
                      3:[21,23],
                      4:[24,27],
                      5:[28,100]
                     }
    print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
    for id,name in stud_dict.items():
        if id in exer_dict:
            if id in exam_dict:
                total_points=exer_dict[f"{'Exercise_Point'} {id}"]+exam_dict[f"{'Exam_Total'} {id}"]
                for point,limit in grade_point_dict.items():
                    if limit[0]<=total_points<=limit[1]:
                        exam_point=point
                        print(f"{name:30}{exer_dict[f"{'Exercise_Total'} {id}"]:<10}{exer_dict[f"{'Exercise_Point'} {id}"]:<10}{exam_dict[f"{'Exam_Total'} {id}"]:<10}{total_points:<10}{exam_point:<10}")
                          
course_grading_3()
