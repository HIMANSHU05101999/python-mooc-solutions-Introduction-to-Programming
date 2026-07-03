# Write your solution here
import urllib.request
import json

def retrieve_course(course_name: str):
    url=f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    url_content=urllib.request.urlopen(url)
    url_data=url_content.read()
    course_data=json.loads(url_data)
    students=[]
    hours=0
    exercises=0
    weeks=0
    for _,line in course_data.items():
        students.append(line['students'])
        hours+=line['hour_total']
        exercises+=line['exercise_total']
        weeks+=1
        
    students=(max(students))
    hours_average=int(hours/students)
    exercises_average=int(exercises/students)
    stats_dict={'weeks':weeks,'students':students,'hours':hours,'hours_average':hours_average,'exercises':exercises,'exercises_average':exercises_average}
    return stats_dict
    
def retrieve_all():
    url="https://studies.cs.helsinki.fi/stats-mock/api/courses"
    url_content=urllib.request.urlopen(url)
    data=url_content.read()
    course_data=json.loads(data)
    
    list_of_tuples=[]
    tup=()
    for line in course_data:
        if line['enabled']==True:
            full_name=(line['fullName'])
            name=(line['name'])
            year=(line['year'])
            exercises=((line['exercises']))
            tup=(full_name,name,year,sum(exercises))
            list_of_tuples.append(tup)
    return list_of_tuples

def main():
    retrieve_all()
    retrieve_course("docker2019")
if __name__=="__main__":
    main()
