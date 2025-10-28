# Journal Application

# this is going to be our function
# to write to the file.
def write_to_journal(file, entry, default_permission=None):
    if default_permission is None:
        default_permission = 'a'
    # if you pass the default_permission as w you're just creating
    # a new file.
    with open(file, default_permission) as file_object:
        # jsut a note:
        # w is going to write over the file
        # a is going to append to the existing items
        # we're going to write but also add a new line
        # so that it doesn't add to the end of the last line.
        file_object.write(F"{entry}\n")

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
        # part one
        # return [F"Error while opening the file {error}"]
        # part two let's create a file and then read, and return those values
        print("file not found, creating one for you")
        write_to_journal(file, '', default_permission='w')
        # we can make this recursive
        # this will always work because we've just created the file.
        return read_journal(file)

# In our journal app we're going to handle three actions
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

    # second that is "w" which is write the to the application
    elif action == "w":
        new_entry = input("Enter entry: ")
        write_to_journal(file, new_entry)
    # to check if it write and write to the file
    # that's the case
    # create a function for this.
    # check to see if the file is found or not.

    # q which is quit

# our application
# make this in a main function.
def main():
    # part one using a defined file path.
    # file_path = "journal.txt"
    # let's make the name a user input
    file_path = input("which journal would you like to use? ")
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