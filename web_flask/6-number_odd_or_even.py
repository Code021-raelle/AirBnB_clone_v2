#!/usr/bin/python3
from flask import Flask, request, render_template

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
    Display 'C ', followed by the value of the text variable,
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

@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """Display 'n is a number' only if n is an integer."""
    if not n.isdigit():
        abort(404)
    return f"{n} is a number"

@app.route('/number_template/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer,
    indicating if the number is odd or even.
    """
    if not n.isdigit():
        abort(404)
    is_even = n % 2 == 0
    return render_template('6-number_odd_or_even.html', n=n, is_even=is_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
