import os
from flask import Flask, render_template, session, flash, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import pymysql.cursors
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
                        flash("Welcome, {}".format(inputUsername.title()))
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
                    flash("Welcome to your dashboard, {}!".format(username).title())
                    return redirect(url_for("dashboard"))

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
            cursor.execute("Select * from session where User = %s order by SessionDate DESC", userid)
            sessiondata = cursor.fetchall()
            cursor.close()
            usersessions = []
            for i in sessiondata:
                usersessions.append(i[0])
            no_duplicates = []
            [no_duplicates.append(n) for n in usersessions if n not in no_duplicates] 
        exerciselist = []

        for x in no_duplicates:
            with connection.cursor() as cursor:
                cursor.execute('''SELECT SessionId, ExerciseId, 
                                    CONCAT(ExerciseTypeName, 
                                    IF(BarTypeName is not null and BarTypeName != '', CONCAT(', ', BarTypeName), ''),
                                    IF(BarPositionName is not null and BarPositionName != '', CONCAT(', ', BarPositionName), ''),
                                    IF(PinHeight is not null and PinHeight <> '' , CONCAT(', ', PinHeight), ''),
                                    IF(SnatchGrip = 1,', Snatch Grip', ''),
                                    IF(Belt is null, '', IF(Belt = 0, ', Beltless' , ', With Belt')),
                                    IF(GripWidthName is not null and GripWidthName != '', CONCAT(', ', GripWidthName), ''),
                                    IF(StanceWidthName is not null and StanceWidthName != '', CONCAT(', ', StanceWidthName), ''),
                                    IF(Pause is not null and Pause <> '' , CONCAT(', ', Pause), ''),
                                    IF(TempoType != '', CONCAT(', Tempo ', TempoType), '')) as ExerciseTextualDescription
                                    FROM gymdb.display_exercise where SessionId = %s''', x)
                exercise = cursor.fetchall()
                exerciselist.append(exercise)
                cursor.close()
        userexercises = []

        def Remove(tuples):
            tuples = [t for t in tuples if t]
            return tuples
       
        emptyTupleRemoved = Remove(exerciselist)
        emptyexremovedlist = list([list(x) for x in emptyTupleRemoved])
        for x in emptyexremovedlist:
            for y in x:
                list(y)
                userexercises.append(y)
        listb = [list(x) for x in userexercises]
        userExIds = []
        for x in listb:
            userExIds.append(x[1])

        sets = []
        for x in userExIds:
            with connection.cursor() as cursor:
                cursor.execute("Select * from sets where ExerciseId = %s", x)
                settuple = cursor.fetchall()
                sets.append(settuple)
                cursor.close()
    return render_template(
            "dashboard.html", listb=listb, sessiondata=sessiondata, sets=sets)


@app.route("/log1", methods=["GET", "POST"])
def log1():
    if request.method == 'POST':
        connection = pymysql.connect(host='localhost', user='root', passwd='', db='gymdb')
        with connection.cursor() as cursor:
            cursor.execute("SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
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
        tuples = tuple([tuple(x) for x in lists])

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
 
        cursor.close()
        usersessions = []
        for i in sessiondata:
            usersessions.append(i[0])
        no_duplicates = []
        [no_duplicates.append(n) for n in usersessions if n not in no_duplicates] 
        print(no_duplicates)
    exerciselist = []

    for x in no_duplicates:
        with connection.cursor() as cursor:
            cursor.execute("select * from display_exercise where SessionId = %s", x)
            exercise = cursor.fetchall()
            exerciselist.append(exercise)
            cursor.close()
    print(exerciselist)
    userexercises = []

    def Remove(tuples):
        tuples = [t for t in tuples if t]
        return tuples
    
    emptyTupleRemoved = Remove(exerciselist)
    emptyexremovedlist = list([list(x) for x in emptyTupleRemoved])
    print(emptyexremovedlist)
    for x in emptyexremovedlist:
        print(x)
        for y in x:
            list(y)
            userexercises.append(y)
    listb = [list(x) for x in userexercises]
    userExIds = []
    for x in listb:
        userExIds.append(x[1])
    print(userExIds)

    sets = []
    for x in userExIds:
        with connection.cursor() as cursor:
            cursor.execute("Select * from sets where ExerciseId = %s", x)
            settuple = cursor.fetchall()
            sets.append(settuple)
            cursor.close()
    print(sets)

    return render_template("log3.html", listb=listb, sessiondata=sessiondata, sets=sets)


@app.route("/edit_session/<SessionId>", methods=["GET", "POST"])
def edit_session(SessionId):
    connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
 
    if request.method == 'POST':
        sessionname = request.form["session-name"]
        sessiondate = request.form['session-date']
        sessiontime = request.form['session-time']
        sessionrpe = request.form['session-rpe']
        sessionid = SessionId
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE session
                SET SessionDate=%s, SessionTime=%s, SessionName=%s, SessionRPE=%s
                WHERE SessionId=%s
                """, (sessiondate, sessiontime, sessionname, sessionrpe, sessionid))
            connection.commit()
            cursor.close()
            flash("Session Updated")
            return redirect(url_for("dashboard"))
    with connection.cursor() as cursor:
        cursor.execute("Select * from session where SessionId = %s", SessionId)
        session = cursor.fetchone()
        cursor.close()
    return render_template("edit_session.html", session=session)


@app.route("/delete_session/<SessionId>")
def delete_session(SessionId):
    connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
    with connection.cursor() as cursor:
        cursor.execute('''
        DELETE FROM session
        where SessionId = %s''', SessionId)
        delete = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        cursor.execute('''
        Select * FROM session''')
        sessions = cursor.fetchall()
        print(delete)
        print(sessions)
    with connection.cursor() as cursor:
        cursor.execute('''
        Select * FROM exercise''')
        exercise = cursor.fetchall()
        print(exercise)
    with connection.cursor() as cursor:
        cursor.execute('''
        Select * FROM sets''')
        sets = cursor.fetchall()
        print(sets)
    connection.commit()

    flash("Session successfully deleted")
    return redirect(url_for("index"))


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