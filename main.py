
from flask import Flask, request,render_template
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

class ProjUser(db.Model):
    __tablename__ = 'ProjUser'
    id = db.Column(db.Integer(), primary_key=True)
    project = db.Column(db.Integer(),db.ForeignKey('Project.id'))
    user = db.Column(db.Integer(),db.ForeignKey('User.id'))

class Project(db.Model):
    __tablename__ = 'Project'
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(50))
    permitTime = db.Column(db.Date())
    startTime = db.Column(db.Date())
    jianshe = db.Column(db.String(50))
    shigong = db.Column(db.String(50))
    sheji = db.Column(db.String(50))
    kancha = db.Column(db.String(50))
    jianli = db.Column(db.String(50),default = "城开监理")
    zaojia = db.Column(db.Float(50))

    diarys = db.relationship('Diary',backref = 'Project',lazy = 'dynamic')



class Diary(db.Model):
    __tablename__ = 'Diary'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date())
    content = db.Column(db.String(255))
    projid = db.Column(db.Integer(),db.ForeignKey('Project.id'))





@app.route('/', methods = ['GET'])
def home():
    res=Diary.query.filter(Diary.projid == 1).first()
    return render_template('home.html',res=res.content)

@app.route('/', methods = ['POST'])
def home_in():
    username = request.form['username']
    password = request.form['password']
  # 这里有一个空值判断strip()
    if username.strip():
        check = User.query.filter(User.username == username).first()
        return render_template('home.html',check = check.username)
    else:
         return render_template('home.html',msg = "请输入名字")

if __name__ == '__main__':
    app.run()

