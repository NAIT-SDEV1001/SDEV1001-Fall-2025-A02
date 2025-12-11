# the testing library that's built in to python
import unittest

# we want to import the tools that we've built in
# the module library_tools

from library_tools.book import Book
from library_tools.library import Library

# to write a test we build on the ideas
# of inheritance.

# we're going to create a class
# that's going to inherit from
# unittest.TestCase
class TestBook(unittest.TestCase):
    # test the constructor
    def test_init(self):
        # check that the properties is
        # what I passed in.
        expected_title = "Dungeon Crawler"
        expected_author = "Matt Dinnamon"
        expected_pages = 643
        # create a book.
        book = Book(
            title=expected_title,
            author=expected_author,
            pages=expected_pages
        )
        # on the unittest.TestCase class that we've
        # inherited from there's a whole bunch of
        # methods like assertEqual that we've inherited
        self.assertEqual(book.title, expected_title)
        self.assertEqual(book.author, expected_author)
        self.assertEqual(book.pages, expected_pages)
        # if you want to make your tests fail before
        # they pass you can use assertNotEqual

    # test the str.
    def test_str(self):
        expected_title = "Dungeon Crawler"
        expected_author = "Matt Dinnamon"
        expected_pages = 643
        # create a book.
        book = Book(
            title=expected_title,
            author=expected_author,
            pages=expected_pages
        )
        # assert that the string are equal
        self.assertEqual(
            str(book),
            F"{expected_title} by {expected_author}"
        )

class TestLibrary(unittest.TestCase):
    # test constructor
    def test_init(self):
        expected_name = "Dans Dandy Dungeon"
        library = Library(expected_name)
        # assertions
        self.assertEqual(library.name, expected_name)
        self.assertEqual(library.books, [])
        # if you wanted to check if the test
        # fails if you do the opposite you can use.
        # self.assertNotEqual(library.name, expected_name)

    # test the str
    def test_str(self):
        expected_name = "Dans Dandy Dungeon"
        library = Library(expected_name)
        self.assertEqual(
            str(library),
            F"Library({expected_name})"
        )

    # test add book
    def test_add_book(self):
        # I need a library created.
        expected_name = "Dans Dandy Dungeon"
        library = Library(expected_name)
        # I need a book that's not added anywhere
        expected_title = "Dungeon Crawler"
        expected_author = "Matt Dinnamon"
        expected_pages = 643
        book = Book(
            title=expected_title,
            author=expected_author,
            pages=expected_pages
        )
        # call the add book function on the instance
        # everything above here is the arrange step
        # of library (act step)
        library.add_book(book)
        # check that the book is in our library
        # in unittest there's assertIn
        # checks to see if something is in an array
        self.assertIn(
            book,
            library.books
        )

    # test list books
    def test_list_books_with_no_books(self):
        """Tests that a library with no books will return None"""
        expected_name = "Dans Dandy Dungeon"
        library = Library(expected_name)
        # this works below because we have
        # an early return with nothing returned
        self.assertIsNone(library.list_books())

    def test_list_books_with_books(self):
        expected_name = "Dans Dandy Dungeon"
        library = Library(expected_name)
        # create some books
        book = Book(
            title="Dans Bio",
            author="Dan",
            pages=10
        )
        bookTwo = Book(
            title="Dans Guide to programming",
            author="Dan",
            pages=20
        )
        # add the books
        library.add_book(book)
        library.add_book(bookTwo)
        # above here is all the arrange step
        # again will return none
        # there's better ways to test this but
        # we're just going to ignore this and
        # move on.

    # test get authors
    def test_get_authors(self):
        expected_name = "Dans Dandy Dungeon"
        library = Library(expected_name)
        # create some books
        book = Book(
            title="Dans Bio",
            author="Dan",
            pages=10
        )
        bookTwo = Book(
            title="Dans Guide to programming",
            author="Dan",
            pages=20
        )
        # add the books
        library.add_book(book)
        library.add_book(bookTwo)

        # above here is the arrange step
        # let's perform the action
        authors = library.get_authors()
        self.assertCountEqual(authors,
                              ["Dan"])
        self.assertListEqual(authors,
                              ["Dan"])


# run the tests.
if __name__ == "__main__":
    unittest.main()