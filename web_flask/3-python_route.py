#!/usr/bin/python3
"""starts a Flask web application on port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=True)
def hello_hbnb():
    """View handler for root url"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=True)
def hbnb():
    """ Returns text response"""
    return "HNBN"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Returns text response"""
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python', strict_slashes=True)
@app.route('/python/<text>', strict_slashes=True)
def python_is_cool(text='is cool'):
    """Returns text response"""
    text = text.replace("_", " ")
    return f'Python {text}'


if __name__ == '__main__':
    app.run()
