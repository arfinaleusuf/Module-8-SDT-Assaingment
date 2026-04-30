class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, Student):
        self.student_list.append(Student)

    

class Student:
    def __init__(self, student_id, name, department, is_enrolled = False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            print('Error: Student Is Already Enrolled')
        else:
            self.__is_enrolled = True