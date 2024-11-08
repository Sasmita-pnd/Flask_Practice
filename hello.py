from flask import Flask

app = Flask(__name__)

@app.route("/Hello")
def hello_world():
    return "<p>I have triggered Hello, World!</p>"

@app.route("/")#Recent Added
def main_page():
    return "<H1>WELCOME TO MY WEBSITE</H1>"