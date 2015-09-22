from flask import Flask

app = Flask(__name__)

# define the directory for the app
@app.route("/about")
def aboutpage():
    page = """
    <h1> About</h1>
    <br>
    <ol>
    <li> About 1 </li>
    <li> About 2 </li>
    <li> About 3 </li>
    """
    return page

@app.route("/lucky")
def lucky_number():
    import random
    r = random.randrange(1,100)
    return "<h1> Lucky Number: %d</h1>" % (r)

@app.route("/home")
@app.route("/")
# define a function to be run everytime someone goes to your app
#      returns a string that represents the homepage
def home():
    return "<h1>Home Page</h1>"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=0000)
    # if host='0.0.0.0' then anybody can access it
    # if host='127.0.0.1' then, it's a localhost
