#!/usr/bin/python3
"""
starting a Flask app
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """
    display a HTML page for cities_by_states
    """
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def teardown_db(arg=None):
    """
    remove the current db Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
