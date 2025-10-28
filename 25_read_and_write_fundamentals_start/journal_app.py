# Journal Application

# In our journal app we're going to handle three actions

def handle_action(action, file):
    print(F"handling {action} on {file}")
    # one that is "r" which is going to list all of the files inside of
    # check if the action is r
    # try to read this file.
    # check to see what the contents of the file are with notes.


    # our application
    # second that is "w" which is write the to the application
    # q which is quit

# make this in a main function.
def main():
    file_path = "journal.txt"
    action = input("Do you want read (r), write (w) or quit (q)")
    # create a while loop that does this
    while action != "q":
        # make make a handler function
        handle_action(action, file_path)
        # ask the user again so that it's a flag.
        action = input("Do you want read (r), write (w) or quit (q)")

# this a better of writing your apps
if __name__ == "__main__":
    main()