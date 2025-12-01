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
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """