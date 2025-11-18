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


if __name__ == "__main__":
    main()