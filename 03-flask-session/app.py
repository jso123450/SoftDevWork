from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/login")
def login():
    return "hello"

@app.route("/about")
def about():
    return "hello"

@app.route("/secret")
def secret():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "shhhh"
    app.run(host='0.0.0.0',port=8000)
