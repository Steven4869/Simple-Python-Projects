class Student:
    college = "Stanford University"
student1 = Student()
student2 = Student()
student1.student_section = "A"
student1.student_name = "Steven Pens"
student1.marks_language = 91
student1.marks_science = 84
student1.marks_math = 99
student2.student_section = "B"
student2.student_name = "Jai"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
