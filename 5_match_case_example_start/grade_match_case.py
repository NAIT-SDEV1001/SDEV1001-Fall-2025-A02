# we're going to get a letter input and we're going to convert to a GPA

print("Welcome to your grade match case calculator")

# .upper is a transformation of text to CAPS
letter_grade = input("Enter your letter grade: ").upper()

# I want you to try to create a variable called gpa
# that will have the following values
# A 4.0
# B 3.3
# C 2.5
# D 2.0
# F 1.0
# I'm setting this to none early
# None is nothing or null or undefined in other languages
gpa = None
# print that letter grade
match letter_grade:
    case "A": # performs the check (letter_grade == "A")
        gpa = 4.0
    case "B": # performs the check (letter_grade == "B")
        gpa = 3.3
    case "C": # performs the check (letter_grade == "C")
        gpa = 2.5
    case "D": # performs the check (letter_grade == "D")
        gpa = 2.0
    case "F": # performs the check (letter_grade == "F")
        gpa = 1.0

    # default case below
    # this is equivalent to an else.
    case _:
        print("Could not parse grade")

# let's do a quick check here if gpa is not None
if not gpa is None:
    print(F"The equivalent GPA is {gpa}")



print(F"letter grade is {letter_grade}")