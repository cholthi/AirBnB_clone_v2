#!/usr/bin/python3
"""
starting a Flask app
"""

from flask import Flask, render_template
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
    txt = text.replace('_', ' ')
    return "C " + txt


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def displayPython(text="is cool"):
    """
    display “Python ”
    """
    txt = text.replace('_', ' ')
    return "Python " + txt


@app.route('/number/<int:n>', strict_slashes=False)
def displayNumber(n):
    """
    display 'n is a number'
    """
    return "{:d} {}".format(n, 'is a number')


@app.route('/number_template/<int:n>')
def displayHTML(n):
    """
    display a HTML page
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOrEven(n):
    """
    display a HTML page for odd or even
    """
    if n % 2 == 0:
        prop = 'even'
    else:
        prop = 'odd'
    return render_template('5-number.html', n=n, prop=prop)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
