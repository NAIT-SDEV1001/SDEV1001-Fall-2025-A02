# docs for the module is here:
# https://docs.python.org/3/library/csv.html
import csv
# I want you to create a function
# that's not only going to take the file path
# the situation (as params) so we don't have duplicates in our
# dataset.
# will return the list of dictionaries using the dictreader
def read_nhl_teams_data(file_path, situation):
    # where we're going to use our csvs.
    try:
        # with open this is going open and close
        # the file once it goes out of scope of the open
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # read all of the lines line by line
            for row in reader:
                breakpoint()
    except FileNotFoundError as error:
        print(F"Error reading the file: {error}")

def get_situation_from_user():
    situations = [
        "other",
        "all",
        "5on5",
        "4on5",
        "5on4",
    ]
    label = "What situation would you like to analyze:\n"
    for index, situation in enumerate(situations):
        label += F"- ({index}) {situation}\n"
    label += "(enter number): "
    print(label)
    # convert this to a number
    user_input_situation = int(input(label))
    # as a note for future importment we could handle the errors
    # that might pop up.
    # return the string of the situation
    return situations[user_input_situation]


# create a main function
# hard code the situations, prompt the for it
# read all of the data
# execute a breakpoint so that you folks can see the data.
def main():
    # filepaths relative to where you are in the
    # folder structure
    file_path = "data/nhl_teams_data_2024_2025.csv"
    situation = get_situation_from_user()
    # get the data using our function to read csv
    teams = read_nhl_teams_data(
        file_path=file_path,
        situation=situation
    )
    breakpoint()

# execute the main
if __name__ == "__main__":
    main()