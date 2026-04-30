class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, Student):
        self.student_list.append(Student)

    @classmethod
    def find_student(self, student_id):
        for student in self.student_list:
            if student.get_student_id == student_id:
                return student
        return False

    @classmethod
    def view_all_students(self):
        if self.student_list:
            for student in self.student_list:
                student.view_student_info()
                print('\n')
        else:
            print("No students found.")

    

class Student:
    def __init__(self, student_id, name, department, is_enrolled = False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    @property
    def get_is_enrolled(self):
        return self.__is_enrolled
    
    @property
    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print('Error: Student is already enrolled')
        else:
            self.__is_enrolled = True
            print(f'student {self.__student_id} has been enrolled')

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'student {self.__student_id} has been droped')
        else:
            print('Error: Student is not enrolled')

    def view_student_info(self):
        print(f'ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}')


s1 = Student('s101','Alice Smith', 'computer seience', True)
s2 = Student('s102','Bob Jonson', 'Mathmatics', False)
s3 = Student('s103','Charlie Lee', 'Physics', True)


def menu():
    while True:
        print('\n --- Student Management Menu ---')
        print('1. View All Students')
        print('2. Enroll Student')
        print('3. Drop Student')
        print('4. Exit')

        choice = input("Enter your choice (1 - 4): ")

        if choice == '1':
            StudentDatabase.view_all_students()
        elif choice == '2':
            student_id = input('Enter Student Id: ')
            student = StudentDatabase.find_student(student_id)

            if student is False:
                print('Error: Invalid Id')
            else:
                student.enroll_student()
        elif choice == '3':
            student_id = input('Enter Student ID to drop: ')
            student = StudentDatabase.find_student(student_id)

            if student is False:
                print('Error: Invalid Student ID')
            else:
                student.drop_student()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invild choice')

menu()