from exam import Exam

class MathExam(Exam):
    def __init__(self, student_name, exam_date, correct_answers, total_questions):
        super().__init__(student_name, exam_date)
        self.correct_answers = correct_answers
        self.total_questions = total_questions
        self.calculate_score()

    def calculate_score(self):
        percent = (self.correct_answers / self.total_questions) * 100
        self.set_score(percent)

    def calculate_grade(self):
        score = self.get_score()
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
