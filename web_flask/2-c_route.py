#!/usr/bin/python3
"""
starting a Flask app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    returns Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def displayC(text):
    """
    returns 'C' followed by the value of the text
    """
    txt = text.replace(i'_', ' ')
    return "C " + txt


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
