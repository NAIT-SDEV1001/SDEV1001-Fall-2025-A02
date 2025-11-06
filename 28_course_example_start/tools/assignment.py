class Assignment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return F"Assignment: {self.name}"

    def __repr__(self):
        return F"Assignment(name={self.name})"
