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
