from operator import truediv
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
