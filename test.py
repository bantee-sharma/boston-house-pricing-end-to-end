from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to flask"

@app.route("/predict")
def hi():
    return "Boston house pricing prediction"