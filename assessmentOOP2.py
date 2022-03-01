class Student:
    #list that store all the instances 
    all_students = []
    all_students_names = []

    def __init__(self, name, grade):
        self.name = name 
        self._grade = grade #property 
        self.__add_student()
        self.__add_student_name()
        

    @property #getter
    def grade(self):
        return self._grade

    @grade.setter #setter
    def grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self._grade = new_grade
        else:
            raise ValueError()

    @staticmethod
    def calculate_average_grade(student_list: list):  #anki, set up an specific argument type 
        if student_list:
            return sum(x._grade for x in student_list)/len(student_list)
        else:
            return -1 

    def __add_student(self):
        Student.all_students.append(self)

    def __add_student_name(self):
        Student.all_students_names.append(self.name)

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) > 0:
            return sum(x._grade for x in cls.all_students)/len(cls.all_students)
        else:
            return -1

    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) > 0:
            scores = ((x._grade, x) for x in cls.all_students)
            return max(scores)[1]
        elif len(cls.all_students) == 1:
            raise ValueError
        else:
            return None


a1 = Student('marcelo',10)
a2 = Student('ernesto',20)
print(a1.calculate_average_grade([a1,a2]))
print(Student.all_students[0].grade)
print(Student.all_students_names)
print(Student.get_best_student())