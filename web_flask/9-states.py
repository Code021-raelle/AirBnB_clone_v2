#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template, request
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML page with a list of all State objects sorted by name."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_detail(id):
    """Display a HTML page with details of a State object and its cities."""
    state = storage.get(State, id)
    if state:
        state.cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def close_session(exception=None):
    """Close the storage after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
