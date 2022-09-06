from flask import Flask, render_template, url_for

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
    return 'created'


if __name__ == '__main__':
    app.run(debug=True)
