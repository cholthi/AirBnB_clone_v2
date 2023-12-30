#!/usr/bin/python3
"""
starting a Flask app
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    display a HTML page
    """
    all_states = sorted(storage.all(State).values(),
                        key=lambda state: state.name)
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def teardown_db(arg=None):
    """
    remove the current db Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
