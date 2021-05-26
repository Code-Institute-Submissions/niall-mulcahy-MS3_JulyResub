import os
from flask import Flask, render_template, session, flash, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.secret_key = 'secret_key'


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


#@app.route("/", methods=["GET", "POST"])
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
    if request.method == 'POST':
        fName = request.form['FirstName'].title()
        lName = request.form['LastName'].title()
        username = request.form['Username'].lower()
        email = request.form['Email'].lower()
        password = generate_password_hash(request.form['Password1'])
        checkRow = (username, email)
        insertRow = (fName, lName, email, username, password)
        connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
        with connection.cursor() as cursor:
            cursor.execute("Select * from user where Username = %s or Email = %s", checkRow,)
            result = cursor.fetchall()
            cursor.close()
            if result:
                print('user already exists')
                return redirect(url_for('register'))
            else:
                print('adding user to db')
                connection = pymysql.connect(
                    host='localhost', user='root', passwd='', db='gymdb')
                with connection.cursor() as cursor:
                    cursor.execute("Insert into user (FirstName, LastName, Email, Username, Password) Values (%s, %s, %s, %s, %s)", insertRow)
                    connection.commit()
                    cursor.close()
                    return render_template("dashboard.html")

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


connection = pymysql.connect(host='localhost', user='root', passwd='', db='gymdb')


connection = pymysql.connect(
        host='localhost', user='root', passwd='', db='gymdb')
with connection.cursor() as cursor:
    cursor.execute('Show tables')
    connection.commit()
    result = cursor.fetchall()
    connection.close()
    print(result)
