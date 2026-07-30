# WRITE YOUR SOLUTION HERE:
class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
            f', grade2: {self.grade2}, grade3: {self.grade3}')

def best_of_all(obj: ExamResult):
    if obj.grade1>obj.grade2 and obj.grade1>obj.grade3:
        return obj.grade1
    elif obj.grade2>obj.grade1 and obj.grade2>obj.grade3:
        return obj.grade2
    else:
        return obj.grade3

def best_results(lists):
    return [best_of_all(object) for object in lists]

if __name__=="__main__":

    result1 = ExamResult("Peter",5,3,4)
    result2 = ExamResult("Pippa",3,4,1)
    result3 = ExamResult("Paul",2,1,3)
    results = [result1, result2, result3]
    print(best_results(results))

