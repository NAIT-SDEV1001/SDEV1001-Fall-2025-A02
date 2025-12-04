import csv
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """

def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings

@app.route('/ufo_sightings', methods=['GET'])
def get_sightings():
    # I want you to get the following from the request.args
    # country (default country is blank)
    country = request.args.get('country', '')
    # page (a number) here default will be one
    page = int(request.args.get('page', 1))
    # size (a number) default is 10
    size = int(request.args.get('size', 10))

    # use the following to test.
    # http://127.0.0.1:5000/ufo_sightings?country=ca&page=1&size=20

    scrubbed_sightings = load_ufo_data('data/scrubbed.csv')

    filtered_sightings = scrubbed_sightings.copy()
    # what I want you to do
    # return the page 1 go from 0 to the size - 1
    # if it's the next page (2) go from size to 2*size -1
    # I also want you to filter on the country only if it's
    # not a an empty string (return all if empty string).
    if country != "":
        for sighting in scrubbed_sightings:
            # if it's not wer're going to remove it.
            if country.lower() != sighting["country"].lower():
                filtered_sightings.remove(sighting)

    # let's do some of the pagination
    min_index = (page - 1)*size
    max_index = page*size - 1

    return jsonify(filtered_sightings[min_index:max_index])

# I want you to add an enpoint that will get the research stations
# return it as json.
