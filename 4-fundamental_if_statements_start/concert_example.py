# two prompts
# one for name of the concert
# second I want you to get if the user has a ticket with y or n
# print it try it out.

# we're going to store the data from the prompt in variables
concert_name = input("What is the name of the concert tonight?")
has_ticket = input("Do you have a ticket (y/n)")

# I want you to print the following
# you're in the right place and have fun
# if the concert name is "taylor swift" and "y" for has ticket
# else
# print this is not the concert your looking for

# here let's take a look at what the operators are doing
# print(concert_name == "taylor swift") # we're checking for equality
# print(has_ticket == "y") # same here.

if concert_name == "taylor swift" and has_ticket == "y":
    print("you're in the right place and have fun")
    # we're going to add some else if
elif concert_name == "metallica":
    print("that concert is next door")
else: # if the above conditions are false
    print("this is not the concert your looking for")


















