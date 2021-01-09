from flask import Flask, render_template

from . import prime_cython as pc
from . import random_name as rn

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/json/')
def json():
    return {"hello": "world"}


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = "Anonymous"
    return render_template("hello.html", name=name)


@app.route('/hello/random')
def hello_random():
    return render_template("hello.html", name=rn.random_name())


@app.route('/primes/')
@app.route('/primes/<int:count>')
def primes(count=None):
    if count is None or count == 0:
        return render_template("primes.html")
    if count > 1000:
        return "Please select a natural number lower or equal to 1000."
    # Return prime.html with list of prime numbers
    return render_template("primes.html", count=str(count),
                           primes=str(pc.primes(count)))
