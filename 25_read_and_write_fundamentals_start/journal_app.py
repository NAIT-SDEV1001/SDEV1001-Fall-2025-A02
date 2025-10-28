# Journal Application

# In our journal app we're going to handle three actions

def read_journal(file):
    try:
        # we're going to use with to read this.
        with open(file, 'r') as file_data:
            # if you want to debug do the following
            data = file_data.readlines()
            # in the above that there's special chars
            # like \n (escape characters)
            # we can remove them with strip
            cleaned_data = []
            for line in data:
                cleaned_data.append(line.strip())
                # strip just removes them.
            return cleaned_data
    except FileNotFoundError as error:
        # we're just going to wrap this in an list
        # so that this prints.
        return [F"Error while opening the file {error}"]

def handle_action(action, file):
    print(F"handling {action} on {file}")
    # one that is "r" which is going to list all of the files inside of
    # check if the action is r
    if action == "r":
        all_lines = read_journal(file)
        for line in all_lines:
            print(line)
        # try to read this file.
    # check to see what the contents of the file are with notes.


    # our application
    # second that is "w" which is write the to the application
    # to check if it write and write to the file
    # that's the case
    # create a function for this.
    # check to see if the file is found or not.

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