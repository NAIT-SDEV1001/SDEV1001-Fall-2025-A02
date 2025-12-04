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
@app.route('/research_stations', methods=['GET'])
def get_research_stations():
    stations = load_ufo_data('data/research_stations.csv')
    return jsonify(stations)


# we're handle a request and give a response.
@app.route('/add_research_station', methods=['POST'])
def add_research_station():
    # I'm going to get the data from the user
    # we're going to do this using `get_json` on the request.
    data = request.get_json() # send the data via json.
    # data above is now going to be a dictionary
    name = data.get('name')
    location = data.get('location')
    # this is where backend development become more of a thing.
    # you 1. validate that the request is good.
    # 2. you need to sanitize the data.
    # we're not going to do this because we're not connected to a database.
    # we're doing a very rudimentary way.
    if not name or not location:
        return jsonify({
            "error": "name and location are required."
        }), 400 # the request status code for bad request
    # everything below is valid ()
    with open('data/research_stations.csv', mode='a', newline='') as file:
        fieldnames = ['name', 'location']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'name': name,
            'location': location
        })
    return jsonify({
        "message": "Research station added successfully"
    }), 201 # the request status code for added successfully
