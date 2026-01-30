from abc import ABC, abstractmethod

class Exam(ABC):
    def __init__(self, student_name, exam_date):
        self.__student_name = student_name
        self.__exam_date = exam_date
        self.__score = 0

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Ball 0 - 100 oralig'ida bo'lishi kerak")

    def get_score(self):
        return self.__score

    def get_student_name(self):
        return self.__student_name

    def get_exam_date(self):
        return self.__exam_date

    @abstractmethod
    def calculate_grade(self):
        pass
