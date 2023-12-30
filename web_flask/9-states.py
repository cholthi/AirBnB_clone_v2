#!/usr/bin/python3
"""
starting a Flask app
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    display a HTML page for /states
    """
    all_states = storage.all(State)
    return render_template('9-states.html',
                          all_states=all_states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
    display a HTML page
    """
    all_states = storage.all(State)
    for state in all_states:
        if state.id == id:
            return render_template('9-states.html',
                                  all_states=all_states, mode='id')
    return render_template('9-states.html',
                          all_states=all_states, mode='none')

@app.teardown_appcontext
def teardown_db(arg=None):
    """
    remove the current db Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
