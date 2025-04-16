
from flask import Flask, request, abort
app = Flask(__name__)


@app.route("/")
def index():
    msg = {"message": "200 OK", "func": "index"}
    return msg


@app.route("/test1")
def test1():
    msg = {"message": "200 OK", "func": "test1"}
    return msg

@app.route("/test2")
def test2():
    msg = {"message": "200 OK", "func": "test2"}

@app.route("/test3")
def test3():
    msg = {"message": "200 OK", "func": "test3"}


@app.route("/post", methods=['POST'])
def post():
    msg = {"message": "200 OK", "func": "post"}
    return msg


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7777)