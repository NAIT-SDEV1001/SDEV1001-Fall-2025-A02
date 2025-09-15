concert_name = input("what is the name of the concert tonight? ")
has_ticket = input("do you have a ticket for the concert? (y/n)")
if concert_name == "Metallica" and has_ticket == "y":
    print("your in the right place")
elif has_ticket == "y":
    print("welcome to the concert")
else:
    print("This is not the right concert for you")