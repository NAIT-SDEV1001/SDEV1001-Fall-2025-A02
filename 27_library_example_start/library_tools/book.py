# all i'm going to do is create the class

# because we have the init files here we can import our
# book into the library.py
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return F"{self.title} by {self.author}"
