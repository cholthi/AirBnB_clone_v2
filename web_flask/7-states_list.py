#!/usr/bin/python3
"""
starting a Flask app
"""

from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    display a HTML page
    """
    all_states = sorted(list(storage.all("State").values()),
            key=lambda x: x.name)
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    remove the current db Session
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
