# create a Book class in a file
# library_tools/book
# the class will have three attributes
# title, author, pages

# __str__ method
# book_title by book_author

# import the book
from library_tools.book import Book
# import the library
from library_tools.library import Library

# to create three books in the main.

# to build on this
# you to create a new file called library
# this should take one argument in the constructor for name
# add_book function take book as an argument
# list_books function take no arguments
# if there are no books in the library then list "No books"
# list_authors function that no arguments lists the authors
# no duplicates.
# add our created books to the library

def main():
    print("Welcome to the library")
    print("----------------------")
    book = Book("Lord of the rings", "Tolkien", 1000)
    bookTwo = Book("Wheel of time", "Jordan", 690)
    bookThree = Book("The Way of Kings", "Sanderson", 1250)
    bookFour = Book("Mistborn", "Sanderson", 640)
    bookFive = Book("Elantris", "Sanderson", 640)

    # let's create our library
    library = Library("Edmonton Public Library")
    library.list_books()

    # add the books one by one,
    library.add_book(book)
    library.add_book(bookTwo)
    library.add_book(bookThree)
    library.add_book(bookFour)
    library.add_book(bookFive)
    print("list books after adding")
    library.list_books()

    print("authors in our library")
    authors = library.get_authors()
    for author in authors:
        print(F"- {author}")

if __name__ == "__main__":
    main()