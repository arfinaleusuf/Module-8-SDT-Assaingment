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

    @property
    def is_enrolled(self):
        return self.__is_enrolled
    
    @property
    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print('Error: Student is already enrolled')
        else:
            self.__is_enrolled = True

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
        else:
            print('Error: Student is not enrolled')