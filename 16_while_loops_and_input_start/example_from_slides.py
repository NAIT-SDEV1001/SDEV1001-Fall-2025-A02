print("Enter numbers to add")
total = 0
while True:
    value = input("enter a number (or done):")
    if value == "done":
        break
        # nothing below this line in the iteration
        # will get executed if the break is hit.
    total += int(value)
    # this is where break points get handy
    breakpoint()
print(F"total sum {total}")