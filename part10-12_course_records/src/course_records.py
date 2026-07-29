# tee ratkaisusi tänne
class Course:
    def __init__(self, name, grade=0, credits=0):
        self.__name=name
        self.__grade=grade
        self.__credits=credits

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self.__grade

    @property
    def credits(self):
        return self.__credits

    @grade.setter
    def grade(self, val):
        self.__grade=val

    @credits.setter
    def credits(self, val):
        self.__credits=val

    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"

class MarkSheet:
    def __init__(self):
        self.__scorecard={}

    def add_course(self, course):
            if course.name in self.__scorecard:
                if self.__scorecard[course.name].grade<course.grade:
                    self.__scorecard[course.name].grade=course.grade

                if self.__scorecard[course.name].credits<course.credits:
                    self.__scorecard[course.name].credits=course.credits
            else:
                self.__scorecard[course.name]=course


    def get_course_data(self, name):
        if name in self.__scorecard:
            print(self.__scorecard[name])
        else:
            print("no entry for this course")

    def to_dict(self):
        return self.__scorecard

    def __str__(self):
        self.__scorecard.__str__()

class Intrerface:
    def __init__(self):
        self.__marksrep=MarkSheet()

    def option(self):
        print("1 add course")
        print("2 get course data")
        print("3 statstics")
        print("0 exit")
        

    def execute(self):
        self.option()
        while True:
            choice=input("choice: ")
            if choice=="1":
                name=input("Course Name: ")
                grade=int(input("Enter Grade: "))
                credit=int(input("Enter Credit: "))
                self.add_course(name,grade,credit)
            if choice=="2":
                name=input("Course Name:")
                self.view_course(name)
            if choice=="3":
                pass
            if choice=="0":
                return

    def view_course(self, name):
        self.__marksrep.get_course_data(name)

    def add_course(self, name, grade, credit):
        course=Course(name,grade,credit)
        self.__marksrep.add_course(course)

    def todict(self):
        return self.__marksrep.__dict__


i=Intrerface()
i.execute()