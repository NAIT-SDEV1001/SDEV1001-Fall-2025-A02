days_of_week = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

# Loop with the day of the week and the index
# if the day has a u in it skip the day.
for index, day in enumerate(days_of_week):

    # let's exit the loop on thurday
    if day == "thursday":
        # exit the loop entirely
        break
        # as a note if you put this below the "u" in day check
        # this will not execute because there's a u in thursday.

    # strings are character arrays in python as well
    # as string which is really nice.
    # if that's true we can use the "in" operator
    # to check if something is in a string.
    if "u" in day:
        # skips the iteration after the continue
        # statement
        continue

    # adding a breakpoint
    # breakpoint()
    print(F"{index}: {day}")
