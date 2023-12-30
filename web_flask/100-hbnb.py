#!/usr/bin/python3
"""
starting a Flask app
"""

from models import storage
from models.amenity import Amenity
from models.state import State
from models.place import Place
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render template with all the states and their amenities
    and places
    """
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    all_places = storage.all(Place)
    return render_template('100-hbnb.html', all_states=all_states,
                           all_amenities=all_amenities,
                           all_places=all_places)


@app.teardown_appcontext
def teardown_db(arg=None):
    """
    remove the current db Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
