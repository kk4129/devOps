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
def primes():
    limit = request.args.get("limit", 100)
    limit = int(limit)

    primes_list = [n for n in range(2, limit+1) if is_prime(n)]

    return render_template(
        "primes.html",
        primes=primes_list,
        limit=limit
    )
