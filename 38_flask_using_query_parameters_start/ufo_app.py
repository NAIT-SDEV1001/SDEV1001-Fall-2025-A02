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



    return jsonify(scrubbed_sightings)

