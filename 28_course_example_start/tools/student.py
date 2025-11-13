class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.submissions = []
    # we're just going to add submissions
    def add_submission(self, submission):
        self.submissions.append(submission)

    def get_submissions(self):
        return self.submissions

    def __str__(self):
        return F"{self.name} ({self.id})"

    def __repr__(self):
        return F"Student(name={self.name}, id={self.id})"
