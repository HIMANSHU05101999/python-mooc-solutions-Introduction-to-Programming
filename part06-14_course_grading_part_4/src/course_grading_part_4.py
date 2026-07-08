# tee ratkaisu tänne
from pathlib import Path
import csv
def course_grading_4(stud_file: str, exer_file: str, exam_file: str, cour_file: str):
    course_detail=Path(__file__).parent/cour_file
    student_deatil=Path(__file__).parent/stud_file
    exercise_detail=Path(__file__).parent/exer_file
    exam_detail=Path(__file__).parent/exam_file
    cour_dict={}
    stud_dict={}
    exe_dict={}
    exa_dict={}
    with open(course_detail) as course_file, open(student_deatil) as s_file, open(exercise_detail) as exe_file, open(exam_detail) as exa_file:
        for line in course_file:
            line=(line.split(":"))
            cour_dict[line[0]]=line[1].strip()
       
        for line in csv.reader(s_file):
            line=(line[0].strip().split(";"))
            if line[0]=='id':
                continue
            stud_dict[line[0]]=f"{line[1]} {line[2]}"

        for line in csv.reader(exe_file):
            temp=[]
            line=(line[0].strip().split(";"))
            if line[0]=='id':
                continue

            for item in line:
                if len(item)>2:
                    continue
                temp.append(int(item))
                exe_dict[line[0]]=temp

        for line in csv.reader(exa_file):
            temp=[]
            line=(line[0].strip().split(";"))
            if line[0]=='id':
                continue

            for item in line:
                if len(item)>2:
                    continue
                temp.append(int(item))
                exa_dict[line[0]]=temp
    calculation(cour_dict,stud_dict,exe_dict,exa_dict)

def calculation(c_dict: dict, s_dict: dict, exe_dict: dict, exa_dict: dict):
    resultstxt=[]
    resultscsv=[]
    grade_point_dict={0:[0,14],
                      1:[15,17],
                      2:[18,20],
                      3:[21,23],
                      4:[24,27],
                      5:[28,100]
                     }
    for id,name in s_dict.items():
        if id in exe_dict:
            if id in exa_dict:
                result_dict={}
                result_dict_csv={}
                total_exercise_num=sum(exe_dict[id])
                total_exercise_pts=sum(exe_dict[id])//4
                exam_points=sum(exa_dict[id])
                total_pts=total_exercise_pts+exam_points
                result_dict_csv['id']=id
                result_dict['name']=name
                result_dict_csv['name']=name
                result_dict['exercise_score']=total_exercise_num
                result_dict['exercise_pts']=total_exercise_pts
                result_dict['exam_pts']=exam_points
                result_dict['total_pts']=total_pts
                
                grade_pts=0
                for grade,limit in grade_point_dict.items():
                    if limit[0]<=total_pts and total_pts<=limit[1]:
                        grade_pts=grade 
                        break
                result_dict['grade']=grade_pts
                result_dict_csv['grade']=grade_pts
            resultstxt.append(result_dict)     
            resultscsv.append(result_dict_csv)                         
    save_txt(c_dict,resultstxt)
    save_csv(resultscsv)

def save_txt(course_data: dict, results_data: list):
    with open("results.txt",'w') as file:
        heading=f"{course_data['name']}, {course_data['study credits']} credits\n"
        file.write(heading)
        border="="*(len(heading)-1)+"\n"
        file.write(border)
        header=f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"
        file.write(header)
        for item in results_data:
            file.write(f"{item['name']:30}{item['exercise_score']:<10}{item['exercise_pts']:<10}{item['exam_pts']:<10}{item['total_pts']:<10}{item['grade']:<10}\n")
    
def save_csv(data: list):
    with open("results.csv",'w',newline="") as file:
        writer=csv.writer(file,delimiter=';')
        for item in data:
            line=(item['id'],item['name'],item['grade'])
            writer.writerow(line)




def main():
    if True:
        student_file=input("Student information:")
        exercise_file=input("Exercises completed:")
        exam_file=input("Exam points:")
        course_detail_file=input("Course information:")
    else:
        course_detail_file="course1.txt"
        student_file="students1.csv"
        exercise_file="exercises1.csv"
        exam_file="exam_points1.csv"
    
    course_grading_4(student_file,exercise_file,exam_file,course_detail_file)
    print("Results written to files results.txt and results.csv")

main()
