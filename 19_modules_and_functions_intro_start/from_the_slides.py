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
