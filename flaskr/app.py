from flask import Flask, render_template, request
import math
from . import prime_cython as pc
from . import random_name as rn

app = Flask(__name__)

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


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
    try:
        # Get limit from query parameter
        limit = request.args.get("limit", 100, type=int)
        
        # Validate input
        if limit < 2:
            limit = 2
        if limit > 10000:  # Prevent very large computations
            limit = 10000
        
        # Generate prime numbers
        primes_list = [n for n in range(2, limit + 1) if is_prime(n)]
        
        return render_template(
            "primes.html",
            primes=primes_list,
            limit=limit
        )
    except (ValueError, TypeError):
        # Handle invalid input
        return render_template(
            "primes.html",
            primes=[],
            limit=100,
            error="Please enter a valid positive number"
        )


if __name__ == '__main__':
    app.run(debug=True)