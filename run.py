import os
from flask import Flask, render_template, session, flash, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors
import pandas as pd
from pandasql import sqldf
import numpy as np
import datetime
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
    if session["user"]:
        connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
            cursor.close()

        with connection.cursor() as cursor:
            cursor.execute("Select * from session where User = %s", userid)
            sessiondata = cursor.fetchall()
            print(sessiondata)
            cursor.close()
            usersessions = []
            for i in sessiondata:
                usersessions.append(i[0])
            print(usersessions)
            no_duplicates = []
            [no_duplicates.append(n) for n in usersessions if n not in no_duplicates] 
            print(no_duplicates)

        exerciselist = []
        with connection.cursor() as cursor:
            sql = ('select ExerciseTypeName from exercisetype')
            cursor.execute(sql)
            exercisetype = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select StanceWidthName from stancewidth')
            cursor.execute(sql)
            stancewidth = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select BarPosition from barposition')
            cursor.execute(sql)
            barposition = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select BarType from bartype')
            cursor.execute(sql)
            bartype = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select Tempo from tempo')
            cursor.execute(sql)
            tempo = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select Pin from pin')
            cursor.execute(sql)
            pin = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select GripWidth from gripwidth')
            cursor.execute(sql)
            gripwidth = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            sql = ('select DeadliftStanceName from deadliftstance')
            cursor.execute(sql)
            deadliftstance = cursor.fetchall()
            cursor.close()
        parameterFinder = (
            exercisetype, stancewidth, gripwidth,
            barposition, bartype, tempo, pin, deadliftstance,)
        
        for x in no_duplicates:
            with connection.cursor() as cursor:
                cursor.execute("select * from exercise where SessionId = %s", x)
                exercise = cursor.fetchall()
                exerciselist.append(exercise)
                cursor.close()
        print(exerciselist)

    return render_template(
            "dashboard.html", sessiondata=sessiondata, exerciselist=exerciselist)


@app.route("/log1", methods=["GET", "POST"])
def log1():
    if request.method == 'POST':
        connection = pymysql.connect(host='localhost', user='root', passwd='', db='gymdb')
        with connection.cursor() as cursor:
            cursor.execute("SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
            print(userid)
            cursor.close()
        sessionname = request.form["session-name"].title()
        sessiondate = request.form['session-date']
        sessiontime = request.form['session-time']
        sessionrpe = request.form['session-rpe']
        sessioninput = (userid, sessiondate, sessiontime, sessionname, sessionrpe)
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO session (User, SessionDate, SessionTime, SessionName, SessionRPE) Values (%s, %s, %s, %s, %s)", sessioninput)
            connection.commit()
            cursor.close()
            flash("Session Created")
            return redirect(url_for("log2"))
    return render_template("log1.html")


@app.route("/log2", methods=["GET", "POST"])
def log2():
    connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
    with connection.cursor() as cursor:
        sql = ('select * from exercisetype order by DisplayOrder, ExerciseTypeName')
        cursor.execute(sql)
        exercisetype = cursor.fetchall()
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

    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
            cursor.close()
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(SessionId) as max_SessionId from session where User = %s", userid)
            sessionid = cursor.fetchall()[0][0]
            cursor.close()
        exercisetypeid = request.form.get('exercisetype')
        stancewidthid = request.form.get('stancewidth')
        gripwidthid = request.form.get('gripwidth')
        barpositionid = request.form.get('barposition')
        bartypeid = request.form.get('bartype')
        beltin = request.form.get('belt')
        tempoid = request.form.get('tempo')
        pausein = request.form.get('pause')
        pinid = request.form.get('pin')
        deadliftstanceid = request.form.get('deadliftstance')
        snatchgripin = request.form.get('snatchgrip')
        exerciseinput = (sessionid, exercisetypeid, stancewidthid, gripwidthid, barpositionid, bartypeid, beltin, tempoid, pausein, pinid, deadliftstanceid, snatchgripin)

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO exercise (SessionId, ExerciseTypeId, StanceWidthId, GripWidthId, BarPositionId, BarTypeId, Belt, TempoId, Pause, PinId, DeadliftStanceId, SnatchGrip) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", exerciseinput)
            connection.commit()
            cursor.close()
        flash("exercise has been logged")

        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(ExerciseId) as max_ExerciseId from exercise where SessionId = %s", sessionid)
            exerciseid = cursor.fetchall()[0][0]
            cursor.close()
        reps = request.form.get('reps')
        weight = request.form.get('weight')
        rpe = request.form.get('rpe')

        reps = request.form.getlist('reps')
        weight = request.form.getlist('weight')
        rpe = request.form.getlist('rpe')
        setszip = zip(reps, weight, rpe)
        listzip = list(setszip)
        lists = [list(x) for x in listzip]
        for x in lists:
            x.insert(0, exerciseid)
        print(lists)
        tuples = tuple([tuple(x) for x in lists])
        print(tuples)

        for x in tuples:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO sets (ExerciseId, Reps, Weight, RPE) VALUES (%s, %s, %s, %s)", x)
                connection.commit()
                cursor.close()
    flash("Sets have been logged")

    return render_template(
        "log2.html", exercisetype=exercisetype, stancewidth=stancewidth,
        barposition=barposition, bartype=bartype,
        tempo=tempo, pin=pin, gripwidth=gripwidth,
        deadliftstance=deadliftstance)


@app.route("/log3", methods=["GET", "POST"])
def log3():
    return render_template("log3.html")


@app.route("/logout", methods=["GET"])
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)


