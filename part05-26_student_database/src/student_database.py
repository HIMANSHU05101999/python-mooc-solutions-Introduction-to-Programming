# Write your solution here
def add_student(student_db: dict,name: str):
    student_db[name]=[]

def add_course(student_db: dict,name: str,course: tuple):
    found=False
    if course[1]!=0:
        #print(student_db)
        for course_name in student_db[name]:
            if course_name[0]==course[0]:
                #print("cond:",course_name[0]==course[0])
                found=True
                if course_name[1]<course[1]:
                    #print("cond2:",course_name[1]<course[1])
                    #found=True
                    student_db[name].remove(course_name)
                    student_db[name].append(course)
        if found==False:            
            student_db[name].append(course)
        #print(student_db)        
    

def print_student(student_db: dict,name: str):
    avg=0
    if name not in student_db:
        print(f"{name}: no such person in the database") 
    else:
        print(f"{name}:")
        if student_db[name]!=[]:
            for i in range(len(student_db[name])):
                avg+=student_db[name][i][1]
            print(f" {len(student_db[name])} completed courses:")    
            for j in range(len(student_db[name])):
                print(f"  {student_db[name][j][0]} {student_db[name][j][1]}")
            print(f" average grade {avg/len(student_db[name])}")
        else:
            print(" no completed courses")
        
def summary(student_db):
    avg=[]
    count=[]
    name=[]
    cnt=0
    sum_score=0
    for student in student_db:
        for courses in student_db[student]:
            cnt+=1
            sum_score+=courses[1]
        avg.append(sum_score/cnt)    
        count.append(cnt)
        name.append(student)
        sum_score=0
        cnt=0

    summ1={}
    for i in range (len(name)):
        for j in range (len(count)):
            for k in range(len(avg)):
                summ1[name[i]]=[count[i],avg[i]]
    temp=0
    temp1=0
    stu_name=""
    stu_name1=""
    for key,val in summ1.items():
        if val[0]>temp:
            temp=val[0]
            stu_name=key
        if val[1]>temp1:
            temp1=val[1]
            stu_name1=key
    most_cmplt=(temp,stu_name)
    highest_avg=(temp1,stu_name1)
    print("students",len(name))
    print(f"most courses completed {most_cmplt[0]} {most_cmplt[1]}")
    print(f"best average grade {highest_avg[0]} {highest_avg[1]}")


def main():
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 0))
    print_student(students, "Peter")
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 5))
    print_student(students, "Peter")
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
if __name__=="__main__":
    main()