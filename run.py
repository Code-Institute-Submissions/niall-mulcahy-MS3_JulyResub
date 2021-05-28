import os
from flask import Flask, render_template, session, flash, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        inputUsername = request.form['Username'].lower()
        inputPassword = request.form['Password1']
        connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
        with connection.cursor() as cursor:
            cursor.execute(
                "select * from user where Username = %s", inputUsername)
            result = cursor.fetchall()
            cursor.close()
            if result:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "select Password from user where Username = %s",
                        inputUsername
                    )
                    returnPassword = cursor.fetchall()
                    cursor.close()
                    if check_password_hash(returnPassword[0][0], inputPassword):
                        session["user"] = request.form.get("Username").lower()
                        return redirect(url_for("dashboard"))
                    else:
                        flash("Username or Password incorrect")
            else:
                flash("Username or password incorrect")
    return render_template("index.html")


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
                flash("Username or Email already exists!")
            else:
                print('adding user to db')
                connection = pymysql.connect(
                    host='localhost', user='root', passwd='', db='gymdb')
                with connection.cursor() as cursor:
                    cursor.execute("Insert into user (FirstName, LastName, Email, Username, Password) Values (%s, %s, %s, %s, %s)", insertRow)
                    connection.commit()
                    cursor.close()
                    session["user"] = request.form.get("Username").lower()
                    flash("Registration was successful!")
                    return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/log1", methods=["GET", "POST"])
def log1():
    return render_template("log1.html")


@app.route("/log2", methods=["GET", "POST"])
def log2():
    connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
    with connection.cursor() as cursor:
        sql = ('select * from exercisetype where ExerciseTypeId < 4')
        cursor.execute(sql)
        exercisetype = cursor.fetchall()
        print(exercisetype)
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from stancewidth')
        cursor.execute(sql)
        stancewidth = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from barposition')
        cursor.execute(sql)
        barposition = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from bartype')
        cursor.execute(sql)
        bartype = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from tempo')
        cursor.execute(sql)
        tempo = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from pin')
        cursor.execute(sql)
        pin = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from gripwidth')
        cursor.execute(sql)
        gripwidth = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        sql = ('select * from deadliftstance')
        cursor.execute(sql)
        deadliftstance = cursor.fetchall()
        cursor.close()
    return render_template(
        "log2.html", exercisetype=exercisetype, stancewidth=stancewidth,
        barposition=barposition, bartype=bartype,
        tempo=tempo, pin=pin, gripwidth=gripwidth,
        deadliftstance=deadliftstance)


@app.route("/log3", methods=["GET", "POST"])
def log3():
    return render_template("log3.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
