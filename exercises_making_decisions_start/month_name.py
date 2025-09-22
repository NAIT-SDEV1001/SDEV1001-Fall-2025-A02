# I'm going to get the input and convert to int.
month_number = int(
    input("Enter a month (1-12): ")
)

print(F"month: {month_number}")

print("Month is:")
# we're going to keep this simple without using
# the date or datetime module
match month_number:
    case 1:
        print("January")
    case 2:
        print("Februrary")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")

    # default case
    case _:
        print("there's only 12 months.")