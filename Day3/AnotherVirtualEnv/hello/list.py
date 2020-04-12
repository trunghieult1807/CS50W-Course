from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie", "David", "Anna"]
    return render_template("list.html", names=names)
