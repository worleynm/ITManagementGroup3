from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello():
    return "Hello, World!"

@app.route("/project_charter")
def hello():
    return "Hello, World!"

@app.route("/team_profile")
def hello():
    return "Hello, World!"