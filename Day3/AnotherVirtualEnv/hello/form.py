from flask import Flask, render_template, request
import webbrowser
webbrowser.open("http://www.example.com")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/hello", methods = ["GET", "POST"])
def submit():
    if request.method == "GET":
        return "Please Fill in the form first"
        open("link.html", "w").write('<a href="http://www.example.com"> Link </a>')
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)
