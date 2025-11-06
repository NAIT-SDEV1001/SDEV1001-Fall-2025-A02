class Submission:
    def __init__(self, student, assignment, grade):
        self.student = student # a Student instance
        self.assignment = assignment # a Assignment instance
        self.grade = grade # a float (decimal number)

    def __str__(self):
        return F"Student: {self.student.name} recieved grade {self.grade} on {self.assignment.name}"
