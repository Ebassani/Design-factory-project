from flask import Flask, render_template, redirect

from flask_login import LoginManager,UserMixin, login_required, login_user, logout_user, current_user

from static.python.functions import *
from static.python.conn_functions import *
from static.python.classes import Accounts

app = Flask(__name__)
app.config['SECRET_KEY'] = '123123123'

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    print(type(user_id))
    cur.execute("SELECT * from accounts where id = (?)", (user_id,))
    info = cur.fetchone()
    if info is None:
        return None
    else:
        return Accounts(int(info[0]), info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/create')
def generate_db():
    create_table()
    create_school('sup', 'hello', 222)
    create_school_account('name@test', 'hello', 1, 'sup')
    create_account('test@feu', 'user1', 'edu', 'bassani', 1, 'pass')
    return 'created'


@app.route('/login')
def verifies_login():
    try:
        user = login('user1', 'pass')
        if len(user) != 1:
            return "something"
        user_id = int(user[0][0])

        login_user(load_user(user_id), remember=True)

        return redirect('/test')
    except:
        return "Log in failed"


@app.route('/test')
@login_required
def test():
    return 'logged in'


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "redirect(somewhere)"


if __name__ == '__main__':
    app.run(debug=True)
