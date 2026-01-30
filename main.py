from math_exam import MathExam
from physics_exam import PhysicsExam
from english_exam import EnglishExam

math = MathExam("Ali", "2026-01-30", 18, 20)
physics = PhysicsExam("Vali", "2026-01-30", 45, 40)
english = EnglishExam("Hasan", "2026-01-30", 80, 75, 85, 90)

print(math.get_student_name(), math.calculate_grade())
print(physics.get_student_name(), physics.calculate_grade())
print(english.get_student_name(), english.calculate_grade())
