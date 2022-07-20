from flask import Flask, render_template, request, redirect, url_for, session
import re
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


# database model
class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):

        return f'<Name {self.username}>'

# ------------------------------------ LOGIN ---------------------------------------------------------------------------


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = Accounts.query.filter_by(username=username, password=password)

        if user:
            session['loggedin'] = True
            session['username'] = str(username)
            session['password'] = str(password)
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)

# ------------------------------------ LOGOUT --------------------------------------------------------------------------


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


# ------------------------------------ REGISTRATION---------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = Accounts.query.filter_by(username=username, password=password, email=email)
        if user:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            session['username'] = str(username)
            session['password'] = str(password)
            session['email'] = str(email)
            db.session.add(user)
            db.session.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)

# ------------------------------------ INIT PAGE -----------------------------------------------------------------------


@app.route("/index")
def index():
    if 'loggedin' in session:
        return render_template("index.html")
    return redirect(url_for('login'))

# ------------------------------------ DISPLAY USER INFO ---------------------------------------------------------------


@app.route("/display")
def display():
    if 'loggedin' in session:
        user = Accounts.query.filter_by(username=session['username'])
        return render_template("display.html", user=user)
    return redirect(url_for('login'))


# ------------------------------------ UPDATE USER INFOS ---------------------------------------------------------------


@app.route("/update", methods=['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            session['username'] = str(username)
            session['password'] = str(password)
            session['email'] = str(email)
            try:
                db.session.commit()
                msg = 'You have successfully updated !'
            except:
                msg = "Failed update"
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template("update.html", msg=msg)
    return redirect(url_for('login'))

# ------------------------------------ MAIN ----------------------------------------------------------------------------


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
