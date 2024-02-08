class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class AttributeFormatterMixin:
    @property
    def formatted_attributes(self):
        attributes = [f"{key}: {getattr(self, key)}" for key in self.__dict__]
        return ", ".join(attributes)

class Student(Person, AttributeFormatterMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

# Example
student = Student("Tamta", "Jashi", 22, "University of Tartu")
print(student.formatted_attributes)

