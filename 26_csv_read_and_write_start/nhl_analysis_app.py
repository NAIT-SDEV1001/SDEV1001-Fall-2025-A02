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
    # list of all_data
    all_data = []
    try:
        # with open this is going open and close
        # the file once it goes out of scope of the open
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # read all of the lines line by line
            for row in reader:
                # we're going to check if the row
                # key of situation is equal to our value
                # append it if that's the case.
                if row["situation"] == situation:
                    all_data.append(row)
    except FileNotFoundError as error:
        print(F"Error reading the file: {error}")
    # lets return this data no matter what.
    return all_data

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

    # convert this to a number
    user_input_situation = int(input(label))
    # as a note for future importment we could handle the errors
    # that might pop up.
    # return the string of the situation
    return situations[user_input_situation]

def get_stat_column_from_user(teams_data):
    # list all of the available columns
    # one of the dictionaries
    all_available_columns = list(teams_data[0].keys())
    label = "Available stat columns\n"
    for index, column in enumerate(all_available_columns):
        label += F"- ({index}): {column}\n"
    label += "Enter the column number to select: "
    choice = int(input(label)) # improvement: handle errors
    # using our knowledge of arrays.
    return all_available_columns[choice]

    # prompt the user to select column to sort by index
    # return the column name from the function

def sort_team_data_by_stat(teams_data, column, reverse=True, top=10):
    # I'm going to create a special function
    # what we're going to use in our sorted function
    def get_column(entry):
        return entry[column]
    breakpoint()
    # descending
    sorted_teams = sorted(teams_data, key=get_column, reverse=reverse)

    # format it
    data = []
    for team_data in teams_data:
        data.append({
            "team": team_data["team"],
            "column": team_data[column]
        })
    return data
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
    teams_data = read_nhl_teams_data(
        file_path=file_path,
        situation=situation
    )

    # created
    column = get_stat_column_from_user(teams_data)

    # sort the team by the stat top x amount
    # using the sorted function
    # function is going to need the following params
    # teams_data, column, reverse=True, top=10
    # sort the teams return an array of dictionaries
    # dict is {team: "name", column: "column"}
    sorted_data = sort_team_data_by_stat(
        teams_data=teams_data,
        column=column
    )


# execute the main
if __name__ == "__main__":
    main()