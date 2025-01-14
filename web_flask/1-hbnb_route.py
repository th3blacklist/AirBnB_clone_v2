#!/usr/bin/python3
"""starts the web app

the app listens on 0.0.0.0, port 5000.
routes:
    /:Display 'Hello HBHB!'
    /:hbnb: displays 'HBNB'
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return ("HBHB")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
