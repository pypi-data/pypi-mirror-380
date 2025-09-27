from .parent_student import Student

class PhDStudent(Student):
    def get_student_type(self):
        return "PhD Student"