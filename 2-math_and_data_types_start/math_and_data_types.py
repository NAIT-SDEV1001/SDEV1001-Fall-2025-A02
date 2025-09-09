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
# the above is using {} wrap the variable days_until_assignment_is_due to use it in the string.
print(statement)


days_in_class_per_week = 3
weeks_in_a_semester = 15
number_of_days_together = days_in_class_per_week * weeks_in_a_semester
print(F"We are seeing each at least {number_of_days_together} days")

number_of_assignments = 4

work_on_assignment_time = weeks_in_a_semester / number_of_assignments

print(F"You'll have about {work_on_assignment_time} weeks per assignment")
# this above even if we're dividing two integers we're getting a float!

# let's do an example where we get an input
number_of_assignments_handed_in_text = input("how many assignments will you hand in (number)? ")
# note you can wrap the input with an int if you'd like.
# let's change this to a number
number_of_assignments_handed_in = int(number_of_assignments_handed_in_text)

# you can do multiple maths on oneline
percent_handed_in = number_of_assignments_handed_in / number_of_assignments * 100
print(F"you're going to hand in {percent_handed_in}% of assignmnets")

# an example of a variable that can't work
# due to python syntax there's no space
# allowed in variables.
# var that does not work = "something"
# the above gives me the following error
#   File "C:\Users\dmouris\lectures\sdev1001-Fall-2025-A02\2-math_and_data_types_start\math_and_data_types.py", line 12
#     var that does not work = "something"
#         ^^^^
# SyntaxError: invalid syntax
