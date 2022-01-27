from os import name
from flask import Flask, url_for
from flask.templating import render_template

FlaskApp = Flask(__name__)

@FlaskApp.route("/")
def hello():
    return '<h1>Klasse</h1>'

@FlaskApp.route("/userinfo1/<username>")
def user(username):
    return render_template('UserInfo1.html', name=username)

@FlaskApp.route("/userinfo2/<username>/<location>/<age_num>")
def user2(username, location, age_num):
    return render_template('UserInfo2.html', name=username, country=location, age=age_num)

if __name__ == "__main__":
    FlaskApp.run()