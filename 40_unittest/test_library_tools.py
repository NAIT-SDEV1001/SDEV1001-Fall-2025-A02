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


# run the tests.
if __name__ == "__main__":
    unittest.main()