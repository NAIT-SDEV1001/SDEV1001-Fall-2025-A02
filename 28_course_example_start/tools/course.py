# the . here is saying look in this folder.
from .student import Student
from .assignment import Assignment

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def bulk_add_students(self, student_data):
        for student_info in student_data:
            self.add_student(
                Student(id=student_info['id'],
                        name=student_info['name'])
            )

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def bulk_add_assignments(self, assignment_data):
        for assignment_info in assignment_data:
            self.add_assignment(
                Assignment(id=assignment_info['id'],
                        name=assignment_info['name'])
            )

    # do the submissions piece.

    def __str__(self):
        return F"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    def __repr__(self):
        return F"Course(name={self.name})"


# import this in the course_app.py
