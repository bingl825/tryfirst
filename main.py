
from flask import Flask, render_template
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
# import db_mod

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    diarys = db.relationship('Diary',backref = 'user',lazy = 'dynamic')

class Diary(db.Model):
    __tablename__ = 'Diary'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date())
    content = db.Column(db.String(255))
    userid = db.Column(db.Integer(),db.ForeignKey('User.id'))

class Project(db.Model):
    __tablename__ = 'Project'
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(255))
    content2 = db.Column(db.String(255))
    content3 = db.Column(db.String(255))
    content4 = db.Column(db.String(255))
    userid = db.Column(db.Integer(),db.ForeignKey('User.id'))

def list_name():
    res = User.query.all()
    list_name = res
    return list_name

@app.route('/')
def home():
    res = list_name()
    return render_template('home.html',list_name = res)

if __name__ == '__main__':
    app.run()

