# the . here is saying look in this folder.
from .student import Student
from .assignment import Assignment
from .submissions import Submission
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
    # submission takes student
    # takes an assignment
    # takes a grade.
    def bulk_add_submissions(self, submission_data):
        for submission_info in submission_data:
            # get a student
            student = self.get_student(
                submission_info["student_id"]
            )

            # get an assignment
            assignment = self.get_assignment(
                submission_info["assignment_id"]
            )
            # create the object
            submission = Submission(
                student=student,
                assignment=assignment,
                grade=submission_info["grade"]
            )
            # add to the students
            student.add_submission(submission)


    # get a student by an id
    def get_student(self, id):
        # loop through the students
        for student in self.students:
            # check if it's the same as the id
            # passed in
            if student.id == id:
                # returning the first match
                return student
        return None

    # get an assignment by an id
    def get_assignment(self, id):
        # loop through the assignments
        for assignment in self.assignments:
            # check if it's the same as the id
            # passed in
            if assignment.id == id:
                # returning the first match.
                return assignment
        return None


    def __str__(self):
        return F"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    def __repr__(self):
        return F"Course(name={self.name})"


# import this in the course_app.py
