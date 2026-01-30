from exam import Exam

class EnglishExam(Exam):
    def __init__(self, student_name, exam_date, reading, writing, speaking, listening):
        super().__init__(student_name, exam_date)
        self.reading = reading
        self.writing = writing
        self.speaking = speaking
        self.listening = listening
        self.calculate_score()

    def calculate_score(self):
        average = (self.reading + self.writing + self.speaking + self.listening) / 4
        self.set_score(average)

    def calculate_grade(self):
        score = self.get_score()
        if score >= 85:
            return "Excellent"
        elif score >= 70:
            return "Good"
        elif score >= 55:
            return "Satisfactory"
        else:
            return "Fail"
