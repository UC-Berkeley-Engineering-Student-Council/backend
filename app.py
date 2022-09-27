# Engineering Student Council Backend
# @author Amol Budhiraja

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
