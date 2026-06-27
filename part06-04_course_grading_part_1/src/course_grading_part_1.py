# write your solution here
from pathlib import Path
def file_processor(file_name: str):
    from pathlib import Path
    #file_name=Path(__file__).parent /file_name
    dictionary={}
    with open(file_name) as file:
        for line in file:
            parts=(line.strip())
            parts=(parts.split(";"))
            if parts[0]=="id":
                continue
            dictionary[parts[0]]=parts[1:]
    return(dictionary)

def student_data_processing(studentdata: dict):
    new_dict={}
    for key,val in studentdata.items():
        new_dict[key]=val[0]+" "+val[1]
    return(new_dict)
    
def exercise_data_processing(exercisedata: dict):
    new_dict={}
    for key, val in exercisedata.items():
        new_list=[]
        for item in val:
            num=int(item)
            new_list.append(num)
        new_dict[key]=sum(new_list)
    return(new_dict)

def main():

    if False:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
    student_data=(file_processor(student_info))
    exercise_data=(file_processor(exercise_data))

    formated_student_data=(student_data_processing(student_data))
    formated_exercise_data=(exercise_data_processing(exercise_data))

    
    for key in formated_student_data:
        if key in formated_exercise_data:
            print(f"{(formated_student_data[key])} {formated_exercise_data[key]}")

            
main()