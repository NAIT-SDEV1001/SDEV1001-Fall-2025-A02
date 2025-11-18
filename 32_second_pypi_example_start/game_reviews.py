# create a virtual env: python -m venv venv
# activate it: venv\Scripts\activate
# install pyexcel: pip install pyexcel
# install pyexcel-xlsx: pip install pyexcel-xlsx
# make a requirements file: pip freeze > requirements.txt
# import pyexcel into this file as pex
import pyexcel as pex # pex is just an alias for pyexcel

def create_game_reviews_excel_file(data, output_file):
    # use the pyexcel module.
    pex.save_as(
        array=data,
        dest_file_name=output_file
    )
    # going to use the method inside of the pyexcel module to save
    # the data.

def add_recommendations_column_to_excel_file(
    input_file, output_file
):
    # get the sheet from excel
    sheet = pex.get_sheet(file_name=input_file)
    # let's get all of the values as an array
    rows = sheet.to_array()
    # create a new array for the recommendation column
    recommendations = ["Recommendations"]

    # loop through every row that isn't a header
    for row in rows[1:]:
        score = row[2] # third value in the row array
        # if the score is above 90
        if score >= 90:
            # add highly recommend
            recommendations.append("Highly Recommend")
        elif score >= 80:
            # it's abouve 80
            # add recommend
            recommendations.append("Recommend")
        elif score >= 70:
            # 70
            # add average
            recommendations.append("Average")
        else:
            # below that
            # do not recommend
            recommendations.append("Tire fire")
    # add a new column with all the values
    sheet.column += recommendations

    sheet.save_as(output_file)


def main():
    # name it this file name.
    GAME_REVIEWS_FILE_NAME = "game_reviews.xlsx"
    # take this data and convert into a xlsx file
    GAME_REVIEWS = [
        ["Title", "Platform", "Score"],
        ["Elden Ring", "PC", 95],
        ["Stardew Valley", "Switch", 89],
        ["Cyberpunk 2077", "PS5", 82],
        ["No Man's Sky", "PC", 90],
        ["Gollum", "PS5", 43],
    ]
    # save the game review data in a file called game_reviews.xlsx
    create_game_reviews_excel_file(
        GAME_REVIEWS,
        output_file=GAME_REVIEWS_FILE_NAME
    )
    add_recommendations_column_to_excel_file(
        input_file=GAME_REVIEWS_FILE_NAME,
        output_file="game_reviews_with_recommendation.xlsx"
    )


if __name__ == "__main__":
    main()
