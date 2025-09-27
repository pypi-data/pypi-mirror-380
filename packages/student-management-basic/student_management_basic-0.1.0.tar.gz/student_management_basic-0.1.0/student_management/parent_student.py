from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    @abstractmethod
    def get_student_type(self):
        pass