print("The ultimate divider")
# make a try block
try:
    num = int(input("Enter a number: "))
    result = 10/num
    print(F"Ulitmate divider result {result}")
except ValueError:
    # the "as error: " is not necessary if you don't care about the message
    print("Sorry that's not a valid number")
except ZeroDivisionError:
    print("Sorry you can't divide by zero")
# note below is clever try not to use this but I thought
# it would be handy for when you see it.
else:
    print("no errors, looks good")
finally:
    # note this will always run but essentially it's not that
    # important here because you can just run this after your
    # try except block.
    print("thank you for using the ultimate divider")