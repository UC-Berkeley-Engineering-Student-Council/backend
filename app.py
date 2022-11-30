# Engineering Student Council Backend
# @author Amol Budhiraja and Ethan Hu

from flask import Flask
from services.newsservice import news_service

app = Flask(__name__)

news_service(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


