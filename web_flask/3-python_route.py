#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display 'C ', followed by the value of the text variable,\
    replacing underscores with spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python', strict_slashes=False)
def python_route(text):
    """
    Display 'Python ', followed by the value of the text variable, 
    replacing underscores with spaces.
    The default value of text is 'is cool'.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
