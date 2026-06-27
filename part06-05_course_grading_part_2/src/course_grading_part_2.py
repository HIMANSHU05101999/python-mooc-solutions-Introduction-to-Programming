# write your solution here
def file_processor(file_name: str):
    #from pathlib import Path
    #file_name=Path(__file__).parent/file_name
    dictionary={}
    with open(file_name) as file:
        for line in file:
            new_line=(line.strip().split(";"))
            if new_line[0]=="id":
                continue
            dictionary[new_line[0]]=new_line[1:]
    return dictionary


def student_file_format(student_data: dict):
    new_dict={}
    for key, val in student_data.items():
        #print(key,val)
        new_dict[key]=val[0]+" "+val[1]
    return new_dict


def exercise_file_format(exercise_data: dict):
    new_dict={}
    
    for key, val in exercise_data.items():
        #print(key,val)
        sum_list=[]
        total_exercise=int(len(val))
        for item in val:
            
            num=int(item)
            sum_list.append(num)
        
        points=sum(sum_list)//4
        new_dict[key]=points
        #print(points)
        #print(sum(sum_list))
    #print("exercise")    
    return(new_dict)
            
def exam_file_format(exam_data: dict):
    new_dict={}
    for key,val in exam_data.items():
        #print(key,val)
        sum=0
        for item in val:
            num=int(item)
            sum+=num
        new_dict[key]=sum
        #print(sum)
    #print("exam")
    return(new_dict)



def main():

    if False:
        student_info=input("Student information:")
        exercise_info=input("Exercises completed:")
        exam_info=input("Exam points:")
    
    else:
        student_info="students2.csv"
        exercise_info="exercises2.csv"
        exam_info="exam_points2.csv"

#    print(file_processor(student_info))
#    print(file_processor(exercise_info))
#    print(file_processor(exam_info))

    read_student=(file_processor(student_info))
    read_exercise=(file_processor(exercise_info))
    read_exam=(file_processor(exam_info))

    formated_student_data=(student_file_format(read_student))
    formated_exercise_data=(exercise_file_format(read_exercise))
    formated_exam_data=(exam_file_format(read_exam))

    dic={}
    dic2={}
    for key,val in formated_exercise_data.items():
        if key in formated_exam_data:
            dic[key]=formated_exercise_data[key]+formated_exam_data[key]
            if dic[key]<=14:
                dic[key]=0
            elif dic[key]>14 and dic[key]<=17:
                dic[key]=1
            elif dic[key]>17 and dic[key]<=20:
                dic[key]=2
            elif dic[key]>20 and dic[key]<=23:
                dic[key]=3
            elif dic[key]>23 and dic[key]<=27:
                dic[key]=4
            elif dic[key]>27:
                dic[key]=5
    #print(dic)
    for key, val in dic.items():
        if key in formated_student_data:
            dic2[formated_student_data[key]]=val
    
    for key, val in dic2.items():
        print(key,val)

main()