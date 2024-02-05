class Student:
    university = "University of Tartu"  

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return self.grade > 60

    def increase_grade(self, increase_amount):
        self.grade += increase_amount


# Example usage:
student1 = Student("Tamta Jashi", 85, 22)
print(student1)  
print(student1.is_passing) 

student1.increase_grade(10)
print(student1)  
print(student1.is_passing)  
