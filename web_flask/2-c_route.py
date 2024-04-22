#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'HelloHBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display 'C ' followed by the value of the text variable,
    replacing underscores with space.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
