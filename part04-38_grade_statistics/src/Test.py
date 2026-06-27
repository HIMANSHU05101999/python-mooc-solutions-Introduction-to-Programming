def split(user_input_score):
    space=user_input_score.find(" ")
    points=int(user_input_score[:space])
    marks=int(user_input_score[space+1:])
    return [points,marks]

def exercise_points(exercise_points):
    return exercise_points//10

def grading(total_points):
    grades=[0,15,18,21,24,28]
    for i in range(5,-1,-1):
        if total_points>=grades[i]:
            return i
        
def mean(user_input):
    return sum(user_input)/len(user_input)


def main():
    points=[]
    grades=[0]*6
    while True:
        user_input=input("Exam points and exercises completed:")
        if user_input=="":
            break
        
        exam_exercise=split(user_input)
        exercise_pnts=exercise_points(exam_exercise[1])
        total_points=exam_exercise[0]+exercise_pnts
        
        points.append(total_points)
        grd=grading(total_points)
        if exam_exercise[0]<10:
            grd = 0 

        grades[grd]+=1
        
        pass_prec = (len(points)-grades[0])/len(points)*100
    print("Statistics:")
    print(f"Points average:{mean(points):.1f}")
    print(f"Pass percentage:{pass_prec:.1f}")
    for i in range (5,-1,-1):
        stars="*"*grades[i]
        print(f"{i}: {stars}")    
main()        
