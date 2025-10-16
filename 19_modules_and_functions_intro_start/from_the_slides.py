# def is equivalent to function in javascript
# def is saying hey I'm defining this function
def greet_user():
    print("hello")
# you need to call it and use it for it do anyting
# greet_user()

# as note, don't use numbers like 1,2,3 in your
# variable names/parameter names
def multiplier(num_one, num_two):
    # as a result of this function
    # i'm going to return a result of
    # the multiplication
    return num_one * num_two
    # you can also return nothing in a function
    # return
    # None is a special data type python
    # that denotes nothing a little undefined in js.

# above is the definition and below we'll get
# different results based on what we pass in
result_one = multiplier(0.01, 9700)

print(F"result_one is {result_one}")

result_two = multiplier(60, 56)

print(F"result_two is {result_two}")
# the function will be behave differently based
# on what you pass in.

# with a return you're assigning the result of
# the function to what you called it with.

# getting with user input
def get_user_favourite_color():
    return input("What is your favourite color? ")

print(F"favourite color is {get_user_favourite_color()}")

# let's function size and names.
# a guideline try to make your function less than 10 lines of code.
# another guideline try to make your functions have 3-5 parameters max.
# what functions allow you to do is not nest your code to 10 tabs (10*4 spaces)
# as a guideline you don't want to have more than 4 (5 sometimes) tabs in your code
# function naming.
# short function names do a lot of things
# longer function names do less things.
# the complexity of your function should be inversely proportional to the name.
# conditions they can be difficult you can create function that
# return true or false normally start these function with is_ or has_
# try to make your function names topical to what you're doing
# you might think this is easy but its' hard.


# default parameter values
def power(number, exponent=None):
    # if this is None then provide a default value
    if exponent is None:
        exponent = 2

    return number ** exponent

# that I didn't actually pass in the two
print(F"3 to power of 2 is {power(3)}")
print(F"3 to power of 4 is {power(3, 4)}")