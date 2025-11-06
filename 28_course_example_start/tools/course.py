# create a Course class
# constructor takes a single argument called name
# create the variables on self.
# name (str)
# students (list)
# a list (list)
# create __str__ that says the name, number of students and assignments
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def __str__(self):
        return F"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    def __repr__(self):
        return F"Course(name={self.name})"


# import this in the course_app.py
