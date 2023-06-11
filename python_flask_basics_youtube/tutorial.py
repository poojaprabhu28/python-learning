# refreshing Python Flask basics
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
    
"""
#basic flask setup
@app.route("/")
def home():
    return "Hello this is the main page <h1>HELLO</h1>"

# display your name on the screen
# display dynamic information
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# redirect unautorised page (here it is admin)
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))
"""

"""
# show dynamic information on the screen
@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["tim", "joe", "bill"])
"""

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

