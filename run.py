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

# Main Home Page route
@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    # Getting the username and password from the form
    if request.method == "POST":
        inputUsername = request.form['Username'].lower()
        inputPassword = request.form['Password1']
        connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')

        # returning the username from the database
        with connection.cursor() as cursor:
            cursor.execute(
                "select * from user where Username = %s", inputUsername)
            result = cursor.fetchall()
            cursor.close()

            # returning the password from the database
            if result:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "select Password from user where Username = %s",
                        inputUsername
                    )
                    returnPassword = cursor.fetchall()
                    cursor.close()

                    # unhashing the password and logging the user in if correct
                    if check_password_hash(returnPassword[0][0], inputPassword):
                        session["user"] = request.form.get("Username").lower()
                        flash("{} is logged in".format(inputUsername.title()))
                        return redirect(url_for("dashboard"))
                    else:
                        flash("Username or Password incorrect")
            else:
                flash("Username or password incorrect")
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # returning data from the registration form
    if request.method == 'POST':
        fName = request.form['FirstName'].title()
        lName = request.form['LastName'].title()
        username = request.form['Username'].lower()
        email = request.form['Email'].lower()

        # using the werkzeug password hash
        password = generate_password_hash(request.form['Password1'])
        checkRow = (username, email)
        insertRow = (fName, lName, email, username, password)

        # connecting to the db
        connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
        
        # checking the db to see if the username or email have been used
        with connection.cursor() as cursor:
            cursor.execute("Select * from user where Username = %s or Email = %s", checkRow,)
            result = cursor.fetchall()
            cursor.close()
            if result:
                flash("Username or Email already exists!")

            # if username and email are available the user is added to the db
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
    # This page cannot be accessed unless the user is in session
    if session["user"]:
        connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
        
        # This block finds the UserId of the logged in user
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
            cursor.close()

        # This block finds all the ssessions completed by this user
        with connection.cursor() as cursor:
            cursor.execute("Select * from session where User = %s order by SessionDate DESC", userid)
            sessiondata = cursor.fetchall()
            cursor.close()

            # I created an empty list to append the session data into
            usersessions = []
            for i in sessiondata:
                usersessions.append(i[0])
            no_duplicates = []
            [no_duplicates.append(n) for n in usersessions if n not in no_duplicates] 

        # Here I created an empty list to append the display_exercise results 
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

        # I wrote this function to remove any sessions with no exercises in it
        def Remove(tuples):
            tuples = [t for t in tuples if t]
            return tuples
       
        # I removed empty tuples from the list and
        # converted the remaining tuples to lists
        # This block allowed me to get the list
        # of exercise ids which belong to the user
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

        # I used the list of ExIds to find the
        # the sets performed by the user
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
    # This page was used to log basic session data
    if request.method == 'POST':
        connection = pymysql.connect(host='localhost', user='root', passwd='', db='gymdb')

        # This found the user id for this user from the db
        with connection.cursor() as cursor:
            cursor.execute("SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
            cursor.close()

        # These statements returned the data from the form
        sessionname = request.form["session-name"].title()
        sessiondate = request.form['session-date']
        sessiontime = request.form['session-time']
        sessionrpe = request.form['session-rpe']
        sessioninput = (userid, sessiondate, sessiontime, sessionname, sessionrpe)

        # This line inputs the session data into the db
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
    
    # This is the exercise input section
    # These cursors all return the various
    # exercise parameters to allow me to populate
    # the html form
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

    # here is where I find the userid
    # and the highest session id for that user
    # This works because the session was just created
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT UserId from user where Username = %s", session["user"])
            userid = cursor.fetchall()[0][0]
            cursor.close()
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(SessionId) as max_SessionId from session where User = %s", userid)
            sessionid = cursor.fetchall()[0][0]
            cursor.close()

        # This is where i returned the values from the form
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

        # I create this tuple to insert into the db
        exerciseinput = (sessionid, exercisetypeid, stancewidthid, gripwidthid, barpositionid, bartypeid, beltin, tempoid, pausein, pinid, deadliftstanceid, snatchgripin)

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO exercise (SessionId, ExerciseTypeId, StanceWidthId, GripWidthId, BarPositionId, BarTypeId, Belt, TempoId, Pause, PinId, DeadliftStanceId, SnatchGrip) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", exerciseinput)
            connection.commit()
            cursor.close()
        flash("exercise has been logged")

        # Here i get the highest exercise id to
        # use for the set insert
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(ExerciseId) as max_ExerciseId from exercise where SessionId = %s", sessionid)
            exerciseid = cursor.fetchall()[0][0]
            cursor.close()
        # took out request.form.get
        # I use the getlist method because there are
        # multiple fields with same name attribute
        reps = request.form.getlist('reps')
        weight = request.form.getlist('weight')
        rpe = request.form.getlist('rpe')

        # I zip the set, weight and rpe tuples together
        # into one tuple
        setszip = zip(reps, weight, rpe)
        listzip = list(setszip)
        lists = [list(x) for x in listzip]

        # I convert them into a list so i can insert the exerciseid value
        # to the beginning of each list
        # This is because they get inserted to the db as
        # exerciseid, reps, weight, rpe
        for x in lists:
            x.insert(0, exerciseid)
        tuples = tuple([tuple(x) for x in lists])

        for x in tuples:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO sets (ExerciseId, Reps, Weight, RPE) VALUES (%s, %s, %s, %s)", x)
                connection.commit()
                cursor.close()

    # These values are populating the exercise input form
    return render_template(
        "log2.html", exercisetype=exercisetype, stancewidth=stancewidth,
        barposition=barposition, bartype=bartype,
        tempo=tempo, pin=pin, gripwidth=gripwidth,
        deadliftstance=deadliftstance)


# This function allows user to change session details only
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

    # This allowed me to return the session data
    with connection.cursor() as cursor:
        cursor.execute("Select * from session where SessionId = %s", SessionId)
        session = cursor.fetchone()
        cursor.close()
    return render_template("edit_session.html", session=session)


@app.route("/delete_session/<SessionId>")
def delete_session(SessionId):
    connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')

    # This deletes the session, the associated exercises
    # and all sets inputted related to those exercises
    # This is achieved with ON DELETE CASCADE when declaring
    # foreign keys in db
    with connection.cursor() as cursor:
        cursor.execute('''
        DELETE FROM session
        where SessionId = %s''', SessionId)
        cursor.close()
    connection.commit()

    flash("Session successfully deleted")
    return redirect(url_for("dashboard"))


# This function allows the user to delete an exercise
# and all associated sets
@app.route("/delete_exercise/<ExerciseId>")
def delete_exercise(ExerciseId):
    connection = pymysql.connect(
            host='localhost', user='root', passwd='', db='gymdb')
    with connection.cursor() as cursor:
        cursor.execute('''
        DELETE FROM exercise
        where ExerciseId = %s''', ExerciseId)
        cursor.close()
    connection.commit()

    flash("Exercise successfully deleted")
    return redirect(url_for("dashboard"))


# Logs the user out by removing the session cookie
@app.route("/logout", methods=["GET"])
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/admin_dash", methods=["GET"])
def admin_dash():
    if session["user"]:
        connection = pymysql.connect(
                host='localhost', user='root', passwd='', db='gymdb')
        
        with connection.cursor() as cursor:
            cursor.execute("select * from session INNER JOIN user on session.User = user.UserId ORDER BY SessionId DESC")
            sessions = cursor.fetchall()
            cursor.close()
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
                                    FROM gymdb.display_exercise''')
            exercises = cursor.fetchall()
            cursor.close()
        with connection.cursor() as cursor:
            cursor.execute("select * from sets")
            sets = cursor.fetchall()
            cursor.close()
        print(sets)
        return render_template("admin_dash.html", sessions=sessions, exercises=exercises, sets=sets)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)