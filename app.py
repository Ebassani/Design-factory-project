from flask import Flask, render_template, redirect, request, Response

from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from static.python.conn_functions import *
from static.python.classes import Accounts
from static.python.functions import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * from accounts where id = (?)", (user_id,))
    info = cur.fetchone()
    if info is None:
        return None
    else:
        return Accounts(int(info[0]), info[1], info[2], info[3], info[4], info[5], info[6],
                        info[7], info[8], info[9], info[10], info[11])


@app.route('/dashboard')
@login_required
def index():  # put application's code here
    update_carbon()
    top3 = False
    topSchools = get_top_schools()[:3]
    currentSchool = ()
    currentSchoolAccount = ()

    for i in get_school_accounts():
        if i[5] == current_user.school_id:
            currentSchoolAccount = i

    for i in get_schools():
        if i[0] == current_user.school_id:
            currentSchool = i

    for i in topSchools:
        if i[0] == currentSchool[1]:
            top3 = True
            break

    if top3:
        return render_template('dashboard.html', schools=topSchools, school=currentSchool,
                               schoolAccount=currentSchoolAccount)

    topSchools.append(currentSchool)
    return render_template('dashboard.html', schools=topSchools, school=currentSchool,
                           schoolAccount=currentSchoolAccount)


@app.route('/')
def introduction():
    return render_template('introduction.html')


@app.route('/currentstate')
def currentstate():
    return render_template('currentstate.html')


@app.route('/create')
def generate_db():
    create_table()
    create_school_account('name@test', 'hello', 'password', 'sup', 654)
    create_account('test@feu', 'user1', 'edu', 'Bassani', 1, 'pass')
    return 'created'


@app.route('/login')
def login():
    return render_template('loginPage.html')


@app.route('/food')
def food():
    return render_template('food.html')


@app.route('/attitude')
def attitude():
    return render_template('attitude.html')


@app.route('/motion')
def motion():
    return render_template('motion.html')


@app.route('/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')


@app.route('/login-authentication', methods=['POST'])
def verifies_login():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        user = finds_user(username, password)

        if len(user) != 1:
            return redirect('/login')
        user_id = int(user[0][0])

        login_user(load_user(user_id), remember=True)

        return redirect('/dashboard')
    except Exception:
        return redirect('/login')


@app.route('/register')
def register_page():
    return render_template('registrationPage.html', schools=get_schools())


@app.route('/register_school')
def school_register_page():
    return render_template('newSchool.html')


@app.route('/create_account', methods=['POST'])
def create_user_account():
    email = request.form.get('email')
    username = request.form.get('username')
    forename = request.form.get('forename')
    surname = request.form.get('surname')
    school_id = request.form.get('school')
    password = request.form.get('password')
    create_account(email, username, forename, surname, school_id, password)
    return verifies_login()


@app.route('/create_school_account', methods=['POST'])
def new_school():
    email = request.form.get('email')
    name = request.form.get('username')
    city = request.form.get('city')
    num_student = request.form.get('num_student')
    password = request.form.get('password')
    create_school_account(email, name, password, city, num_student)
    return verifies_login()


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
