from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello World"
    return render_template("hello.html", headline=headline)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"

@app.route("/render")
def render():
    return render_template("day2.html")
