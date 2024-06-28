from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    enteredName = request.args.get("name", "world")
    return render_template("index.html", name=enteredName)
