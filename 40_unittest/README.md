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

Check that the book and library does what we expect.