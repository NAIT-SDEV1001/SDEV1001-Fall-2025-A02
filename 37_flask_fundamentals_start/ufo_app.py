import csv
# import a few things from flask.
from flask import Flask, request, jsonify

# to create an app here we need to call Flask
app = Flask(__name__)

# let's create a home page.
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>

        </head>
        <body>
            <h1>Welcome to the UFO Sightings API😀</h1>
            <p>Use the /ufo_sightings route to get UFO sighting data.</p>
            <ul></ul>
            <script defer>
            let list = document.querySelector('ul')
            // fetch to the backend
            const getSightings = async () => {
                const response = await fetch('/ufo_sightings')
                return await response.json()
            }
            document.addEventListener("DOMContentLoaded",async () => {
                const sightings = await getSightings()
                sightings.forEach((sighting) => {
                    list.innerHTML += `<li>
                        ${sighting.city}: ${sighting.datetime}
                    </li>`
                })
            })

            </script>
        </body>
    </html>
    """

ufo_sightings = [
    {
        "datetime": "10/10/1949 20:30",
        "city": "san marcos",
        "state": "tx",
        "country": "us",
        "shape": "cylinder",
        "duration (seconds)": "2700",
        "duration (hours/min)": "45 minutes",
        "comments": "This event took place in early fall around 1949-50. It occurred after a Boy Scout meeting in the Baptist Church. The Baptist Church sit",
        "date posted": "4/27/2004",
        "latitude": "29.8830556",
        "longitude": "-97.9411111"
    },
    {
        "datetime": "10/10/1949 21:00",
        "city": "lackland afb",
        "state": "tx",
        "country": "",
        "shape": "light",
        "duration (seconds)": "7200",
        "duration (hours/min)": "1-2 hrs",
        "comments": "1949 Lackland AFB&#44 TX.  Lights racing across the sky &amp; making 90 degree turns on a dime.",
        "date posted": "12/16/2005",
        "latitude": "29.38421",
        "longitude": "-98.581082"
    }
]

# create a function that's not a route but will just load the data
def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings


# create ufo sightings
# http://localhost:5000/ufo_sightings
@app.route('/ufo_sightings', methods=['GET'])
def get_sightings():
    # instead of using the sightings above here
    # I want you to essentally load the data form the
    # scrubbed csv
    # return that data.
    file = "data/scrubbed.csv"
    sightings = load_ufo_data(file)
    # we're getting query parameters
    city = request.args.get('city', '')
    if city == "": # if it's blank return the first ten sightings
        return jsonify(sightings[:10])
    # below here we're searching for those values
    # searchable by city.
    filtered_sightings = []
    for sighting in sightings:
        # a substring is another
        if city.lower() in sighting["city"].lower():
            filtered_sightings.append(sighting)

    return jsonify(filtered_sightings[:10]) # return the first 10
