from flask import Flask, render_template
from . import prime_cython as pc

app = Flask(__name__)

hello_message = "This is a message from flask!"

@app.route('/')
def index():
    return render_template("index.html", message=hello_message)

@app.route('/json/')
def json():
    return {"hello":"world"}

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name == None:
        name = "Anonymous"
    return "Hello " + str(name) + "."

@app.route('/primes/')
@app.route('/primes/<int:count>')
def primes(count=None):
    if count == None:
        count = 100   
    elif count > 1000:
        return "Please select a natural number lower or equal to 1000."     
    # Return prime.html with list of prime numbers
    return render_template("prime.html", count=str(count), primes=str(pc.primes(count)))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
