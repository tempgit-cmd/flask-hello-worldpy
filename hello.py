# Shamelessly copied but also modfied to print numbers from 1 to 10 so the shameless owner of this repo could read and code better from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    # Now you have some shame i have modified this to also print 1 to 10!
    numbers = " ".join(str(i) for i in range(1, 11))
    return f"Hello World! Here are the numbers: {numbers}"

if __name__ == '__main__':
    app.run()

