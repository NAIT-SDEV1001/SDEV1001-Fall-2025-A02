# A Small Introduction to unittest.

A few a libraries that are available for us to test.

- [unittest](https://docs.python.org/3/library/unittest.html)
  - built into the standard library
- [pytest](https://docs.pytest.org/en/stable/)

Testing across langauges is fairly consistent they always follow the same pattern.
  - each test is going to have
    - arrange (set it up, everything you need)
    - act (do the thing that you want to test)
    - assertion (does the thing do what you expect)

Testing is much more important on the backend then it is on the frontend.

## Running tests in python.

`python -m unittest <the-name-of-the-testing-file>`

There's other ways to run it, this is the way we're going to do it today.


## What we're going to do

Check that the `Book` and `Library` classes in the `library_tools` module do what we expect.

This also builds upon our knowledge of inheritance that we've done (and if you haven't done it it's a way to add functionality to a class).

## Steps.

### 1. Create a file called `test_library_tools.py` in the same folder as the file `library_app.py`.

### 2. In that file import `unittest` and your library module and book.
```python
# the testing library that's built in to python
import unittest

# we want to import the tools that we've built in
# the module library_tools

from library_tools.book import Book
from library_tools.library import Library
```
### 3. Let's create our first test class for our `Book` class (no tests yet)

In the file `test_library_tools.py` create a class named `TestBook` that inherits the class `unittest.TestCase` it should look a bit like below.

```python
class TestBook(unittest.TestCase):
    pass
```

Now that we have our first environment here let's take at what happens when we run the tests.
Run the tests with the following command:
`python -m unittest test_library_tools.py`

You should see the following output
```
$ python -m unittest test_library_tools.py

----------------------------------------------------------------------
Ran 0 tests in 0.000s

NO TESTS RAN
```
Now there's no tests that we've defined here


