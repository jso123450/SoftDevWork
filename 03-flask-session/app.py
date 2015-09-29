from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method="GET":
        return render_template("login.html")
    else:
        un = request.form["username"]
        pw = request.form["password"]

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/secret")
def secret():
    return render_template("secret.html")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "shhhh"
    app.run(host='0.0.0.0',port=8000)
