#!/usr/bin/python3
"""starts a Flask web application on port 5000
Provides url route at /
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=True)
def hello_hbnb():
    """View handler for root url"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
