"""
Object-Oriented Programming implementation
By: Teagan Laws, assisted by ChatGPT
Date: 12 February 2023
"""


class Student:
    def __init__(self, name, student_id, student_name, marks):
        self.name = name
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks


class Marks:
    def __init__(self, subject, marks_obtained, maximum_marks):
        self.subject = subject
        self.marks_obtained = marks_obtained
        self.maximum_marks = maximum_marks


class Undergraduate(Student):
    def __init__(self, name, student_id, student_name, marks, sat_score):
        super().__init__(name, student_id, student_name, marks)
        self.sat_score = sat_score


class Postgraduate(Student):
    def __init__(self, name, student_id, student_name, marks, bachelors_gpa):
        super().__init__(name, student_id, student_name, marks)
        self.bachelors_gpa = bachelors_gpa


# create a list of students
students = [
    Undergraduate("Mark", "1001", "Computer Science", [Marks("Maths", 80, 100), Marks("Physics", 90, 100)], 1200),
    Postgraduate("Sam", "2001", "Data Science", [Marks("Data Mining", 85, 100), Marks("Machine Learning", 95, 100)],
                 3.8),
    Undergraduate("Jane", "1002", "Mechanical Engineering", [Marks("Mechanics", 75, 100), Marks("Thermodynamics", 85,
                                                                                                100)], 1300),
    Postgraduate("Chris", "2002", "Artificial Intelligence", [Marks("Natural Language Processing", 80, 100),
                                                              Marks("Computer Vision", 90, 100)], 3.6),
]

# iterate over the list and show student details
for student in students:
    print(f"Name: {student.name}")
    print(f"Student ID: {student.student_id}")
    print(f"Degree: {student.student_name}")
    print("Marks:")
    for mark in student.marks:
        print(f"- {mark.subject}: {mark.marks_obtained}/{mark.maximum_marks}")
    if isinstance(student, Undergraduate):
        print(f"SAT Score: {student.sat_score}")
    elif isinstance(student, Postgraduate):
        print(f"Bachelor's GPA: {student.bachelors_gpa}")
    print()
