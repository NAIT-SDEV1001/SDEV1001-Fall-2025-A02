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

    # strings are character arrays in python as well
    # as string which is really nice.
    # if that's true we can use the "in" operator
    # to check if something is in a string.
    if "u" in day:
        continue

    # let's exit the loop on thurday

    # adding a breakpoint
    # breakpoint()
    print(F"{index}: {day}")
