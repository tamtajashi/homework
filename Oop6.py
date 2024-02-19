class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.__grades = {}

    def add_grade(self, subject, grade):
        self.__grades[subject] = grade

    def average_grade(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def display_details(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Average Grade: {self.average_grade()}")


class StudentManagementSystem:
    def __init__(self):
        self.__students = {}

    def add_student(self, student_id, name):
        if student_id not in self.__students:
            self.__students[student_id] = Student(student_id, name)
            print("Student added successfully.")
        else:
            print("Student already exists with the same ID.")

    def show_student_details(self, student_id):
        student = self.__students.get(student_id)
        if student:
            student.display_details()
        else:
            print("Student not found.")

    def show_student_average_grade(self, student_id):
        student = self.__students.get(student_id)
        if student:
            print(f"Average grade for student {student_id}: {student.average_grade()}")
        else:
            print("Student not found.")


# Example Usage
if __name__ == "__main__":
    sms = StudentManagementSystem()

    sms.add_student(101, "Alice")
    sms.add_student(102, "Bob")

    sms.show_student_details(101)
    sms.show_student_details(102)

    sms.add_student(101, "Charlie")  # Trying to add duplicate student

    sms.show_student_average_grade(101)
