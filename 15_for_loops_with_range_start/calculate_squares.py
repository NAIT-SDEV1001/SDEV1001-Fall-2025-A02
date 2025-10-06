# I want you to
# loop over a range
# I want you folks start at 0 end at 100 and step by 12
# I want you to print out the squares of those values.
START = 0
END = 100
STEP = 12

# let's use this variables in our function
# they are caps because they're viewed as constants
for your_variable in range(START, END, STEP):
    print(F"value of i is {your_variable} the square is {your_variable**2}")
    # this is indented piece will execute each iteration.
