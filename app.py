from flask import Flask, render_template

from static.python.functions import *
from static.python.conn_functions import *

app = Flask(__name__)


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


@app.route('/login', methods=['POST'])
def verifies_login():
    try:
        user = login('user1', 'pass')
        if len(user) > 1:
            return "something"
        global user_id
        user_id = int(user[0][0])
        return "logged in"
    except:
        return "not logged in"


if __name__ == '__main__':
    app.run(debug=True)
