class Library:
    def __init__(self, name):
        # create a couple of variables here
        # on self: name, books
        self.books = []
        self.name = name

    def __str__(self):
        return F"Library({self.name})"

    def add_book(self, book):
        # add it to the array
        self.books.append(book)

    def list_books(self):
        if len(self.books) == 0:
            print("No books in the library")
            return # early return so less nesting.

        for book in self.books:
            print(F"- {book}")
            # note this will print out the books
            # from the __str__ method we created
                # the book.

    def get_authors(self):
        # loop through and get the author
        # my knowledge of set theory
        # docs: https://docs.python.org/3/tutorial/datastructures.html#sets

        all_authors = []
        for book in self.books:
            all_authors.append(book.author)

        # this will remove all duplicates below
        return list(set(all_authors))
