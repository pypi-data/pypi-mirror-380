from .parent_student import Student

class UndergraduateStudent(Student):
    def get_student_type(self):
        return "Undergraduate Student"