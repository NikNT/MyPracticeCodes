# Class methods - Allows operation related to the class itself - take cls as the first parameter

class Student:
    count = 0
    total_gpa = 0.0

    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def getInfo(self):
        return f'Student : {self.name} GPA {self.gpa}'
    
    @classmethod
    def getCount(cls):
        return f'Count: {cls.count}'
    
    @classmethod
    def totalGpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'Avg GPA : {cls.total_gpa / cls.count:.2f}'
        

print(Student.getCount())

student1 = Student("Spongebob", 3.8)
student2 = Student("Patrick", 2.5)
student3 = Student("Sandy", 4.0)

print(Student.getCount())
print(Student.totalGpa())