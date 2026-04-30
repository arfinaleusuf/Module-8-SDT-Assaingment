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
    def student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print('Error: Student is already enrolled')
        else:
            self.__is_enrolled = True
            print(f'student {self.student_id} has been enrolled')

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'student {self.student_id} has been droped')
        else:
            print('Error: Student is not enrolled')

    def view_student_info(self):
        print(f'ID: {id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}')


s1 = Student(101,'Alice Smith', 'computer seience', True)
s2 = Student(102,'Bob Jonson', 'Mathmatics', False)
s3 = Student(103,'Charlie Lee', 'Physics', True)