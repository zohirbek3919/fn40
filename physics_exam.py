from exam import Exam

class PhysicsExam(Exam):
    def __init__(self, student_name, exam_date, lab_score, theory_score):
        super().__init__(student_name, exam_date)
        self.lab_score = lab_score
        self.theory_score = theory_score
        self.calculate_score()

    def calculate_score(self):
        total = self.lab_score + self.theory_score
        self.set_score(total)

    def calculate_grade(self):
        score = self.get_score()
        if score >= 90:
            return 5
        elif score >= 75:
            return 4
        elif score >= 60:
            return 3
        else:
            return 2
