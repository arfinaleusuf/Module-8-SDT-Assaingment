class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, Student):
        self.student_list.append(Student)

    

class Student:
    def __init__(self, student_id, name, department, is_enrolled = False):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled