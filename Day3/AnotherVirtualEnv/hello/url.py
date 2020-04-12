from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("url.html")

@app.route("/more")
def more():
    return render_template("day2.html")
