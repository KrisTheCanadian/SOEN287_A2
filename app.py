from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/hackathon')
def hack():
    return render_template("hack.html")


@app.route('/experience')
def exp():
    return render_template("exp.html")


@app.route('/freelancing')
def free():
    return render_template("freelance.html")


@app.route('/education')
def edu():
    return render_template("education.html")


@app.route('/testimonials')
def testi():
    return render_template("testimonials.html")


if __name__ == '__main__':
    app.run()
