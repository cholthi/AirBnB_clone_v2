#!/usr/bin/python3
"""starts a Flask web application on port 5000
"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=True)
def is_number(n):
    """Returns a text response"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=True)
def number_template(n):
    """Returns a html encoded response"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=True)
def template_odd_even(n):
    """Returns html encoded respoonse"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run()
