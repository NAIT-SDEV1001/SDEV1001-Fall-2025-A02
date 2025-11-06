class Submission:
    def __init__(self, student, assignment, grade):
        self.student = student # a Student instance
        self.assignment = assignment # a Assignment instance
        self.grade = grade # a float (decimal number)
        self.letter_grade = self._assign_letter_grade() # needs to be under grade assignment.

    # python has nothing that's private
    # "_" denotes private function (should only be used in the class)
    # this is a convention for variables and functions.
    def _assign_letter_grade(self):
        if self.grade > 90:
            return "A"
        if self.grade > 80:
            return "B"
        if self.grade > 70:
            return "C"
        if self.grade > 60:
            return "D"
        if self.grade <= 60:
            return "F"
        return "F"

    def __str__(self):
        return F"Student: {self.student.name} recieved grade {self.grade} on {self.assignment.name}"
