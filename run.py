import os
from flask import Flask, render_template, session, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
# def signin():
#   build connection to sql database
#   store the username and password as variables here
#   
#   if request.method == "POST":
#       existing_user = variable stored above
#   if existing_user:
#       if check_password_hash(
#       existing_user["password"]), request.form.get("password")):
#           session["user"] = request.form.get("username").lower
    


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/log", methods=["GET", "POST"])
def log1():
    return render_template("log1.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)