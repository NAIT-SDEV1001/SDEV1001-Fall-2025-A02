# create a variable
# they use something called snake case
# snake_case_looks_like_this
# essentially has underscores for space
days_until_assignment_is_due = 14
# the above is an integer because it's
# a whole number


# let's talk about f-strings
# this is a way to print out things in a string
statement = F"Assignment due in {days_until_assignment_is_due} days"
print(statement)

# an example of a variable that can't work
# due to python syntax there's no space
# allowed in variables.
# var that does not work = "something"
# the above gives me the following error
#   File "C:\Users\dmouris\lectures\sdev1001-Fall-2025-A02\2-math_and_data_types_start\math_and_data_types.py", line 12
#     var that does not work = "something"
#         ^^^^
# SyntaxError: invalid syntax
