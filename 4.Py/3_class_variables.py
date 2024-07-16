# Class variables - defined outside the constructor and share amongst all instances 

class Student:
    class_year = 2024
    count = 0
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Student.count += 1

    @classmethod
    def getClassYear(cls):
        return cls.class_year
    
    @classmethod
    def getTotalStudents(cls):
        return cls.count

student1 = Student('Spongebob', 30)
student2 = Student('Patrick', 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name, student1.age, student1.class_year, student1.getClassYear())
print(student2.name, student2.age, student2.class_year)
print(Student.class_year, Student.count)
print(f'My graduating class of {Student.class_year} has {Student.getTotalStudents()} students')
