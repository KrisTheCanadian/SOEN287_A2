from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/hello')
def hello_soen287():
    return '<h1>Hello SOEN287!</h1>'


if __name__ == '__main__':
    app.run()


