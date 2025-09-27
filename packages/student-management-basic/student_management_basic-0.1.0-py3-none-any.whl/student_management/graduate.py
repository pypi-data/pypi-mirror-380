from .parent_student import Student

class GraduateStudent(Student):
    def get_student_type(self):
        return "Graduate Student"