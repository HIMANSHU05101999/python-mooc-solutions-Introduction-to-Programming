# Write your solution here
def split(user_input_score):
    first_part_of_score=""
    second_part_of_score=""
    for i in range(0,len(user_input_score)):
        if user_input_score[i]==" ":
            (first_part_of_score)=int(user_input_score[:i])
            (second_part_of_score)=int(user_input_score[i+1:])
    return (first_part_of_score,second_part_of_score)
  
        
def calculation_of_the_scores(score_1,score_2):
    failed_counter=0
    exercise_point=0    
    if  (score_2>=10 and score_2<20):
            exercise_point+=1
    elif (score_2>=20 and score_2<30):
            exercise_point+=2
    elif (score_2>=30 and score_2<40):
            exercise_point+=3
    elif (score_2>=40 and score_2<50):
            exercise_point+=4
    elif (score_2>=50 and score_2<60):
            exercise_point+=5
    elif (score_2>=60 and score_2<70):
            exercise_point+=6
    elif (score_2>=70 and score_2<80):
            exercise_point+=7
    elif (score_2>=80 and score_2<90):
            exercise_point+=8
    elif (score_2>=90 and score_2<100):
            exercise_point+=9
    elif (score_2==100):
            exercise_point+=10
    else:
            exercise_point+=0
    final_points=score_1+exercise_point        
    if score_1<10 or final_points<15:
            failed_counter+=1        
    return(final_points,failed_counter)
    
   
def final_point_grading(point,total_point):
    grade_5=0
    grade_4=0
    grade_3=0
    grade_2=0
    grade_1=0
    grade_0=0

    if total_point>=0 and total_point<=14 and point>=10:
            grade_0+=1
    elif total_point>=15 and total_point<=17 and point>=10:
            grade_1+=1
    elif total_point>=18 and total_point<=20 and point>=10:
            grade_2+=1
    elif total_point>=20 and total_point<=23 and point>=10:
            grade_3+=1    
    elif total_point>=24 and total_point<=27 and point>=10:
            grade_4+=1
    elif total_point>=28 and total_point<=30 and point>=10:
            grade_5+=1    
    else:
           grade_0+=1
    return (grade_0,grade_1,grade_2,grade_3,grade_4,grade_5)

   

def main():
    count=0
    avg_point=0

    point_score=0
    point=0
    score=0

    point_and_fail=0
    total_points=0
    fail=0

    final_grades=0
    grade0=0
    grade1=0
    grade2=0
    grade3=0
    grade4=0
    grade5=0

    while True:
        user_input=input("Exam points and exercises completed:")
        #user_input="12 110"
        if user_input=="":
            print("Statistics:")
            break
        count+=1
        point_score=(split(user_input))
        #print(point_score)
        point=point_score[0]
        score=point_score[1]
#        print(f"Exam point: {point}")
#        print(f"Exercise completed: {score}")

    
               
        point_and_fail=(calculation_of_the_scores(point,score))
#        print(point_and_fail)
        total_points=point_and_fail[0]
        fail+=point_and_fail[1]
        avg_point+=total_points
#        print(f"Exam point+ Exrcise complete: {avg_point}")
#        print(f"Failed: {fail}")

        final_grades=final_point_grading(point,total_points)
        grade0+=final_grades[0]
        grade1+=final_grades[1]
        grade2+=final_grades[2]
        grade3+=final_grades[3]
        grade4+=final_grades[4]
        grade5+=final_grades[5]
#        print("Grade 0",grade0)
#        print("Grade 1",grade1)
#        print("Grade 2",grade2)
#        print("Grade 3",grade3)
#        print("Grade 4",grade4)
#        print("Grade 5",grade5)
    
    #print("Statistics:")
    print(f"Points average: {avg_point/count} ")
    print(f"Pass percentage: {100-(fail/count)*100:.1f}")
    print("Grade distribution:")
    print(f" 5: {"*"*grade5}")
    print(f" 4: {"*"*grade4}")
    print(f" 3: {"*"*grade3}")
    print(f" 2: {"*"*grade2}")
    print(f" 1: {"*"*grade1}")
    print(f" 0: {"*"*grade0}")
main() 





