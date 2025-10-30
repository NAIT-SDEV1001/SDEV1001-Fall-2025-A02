# I want you to create a function
# that's not only going to take the file path
# the situation (as params) so we don't have duplicates in our
# dataset.
# will return the list of dictionaries using the dictreader

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


# execute the main
if __name__ == "__main__":
    main()