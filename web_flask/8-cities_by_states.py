#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of all State objects
    and their cities sorted by name.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(exception=None):
    """Close the storage after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
