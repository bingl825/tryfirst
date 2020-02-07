
from flask import Flask, request, render_template, g, session, abort, url_for, redirect
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def get_id(self):
        return int(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymouse(self):
        return False


class ProjUser(db.Model):
    __tablename__ = 'ProjUser'
    id = db.Column(db.Integer(), primary_key=True)
    project = db.Column(db.Integer(), db.ForeignKey('Project.id'))
    user = db.Column(db.Integer(), db.ForeignKey('User.id'))

class Project(db.Model):
    __tablename__ = 'Project'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    permitTime = db.Column(db.Date())
    startTime = db.Column(db.Date())
    jianshe = db.Column(db.String(50))
    shigong = db.Column(db.String(50))
    sheji = db.Column(db.String(50))
    kancha = db.Column(db.String(50))
    jianli = db.Column(db.String(50), default= "城开监理")
    zaojia = db.Column(db.Float(50))

    diarys = db.relationship('Diary', backref='Project', lazy='dynamic')



class Diary(db.Model):
    __tablename__ = 'Diary'
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date())
    content = db.Column(db.String(255))
    projid = db.Column(db.Integer(), db.ForeignKey('Project.id'))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remenber_me = BooleanField('renmenber_me', default=False)




@app.before_request
def before_requset():
    g.user = current_user

#--user_loader回调
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = "first post."
    return render_template('index.html', title="home", user=user, posts=posts)


@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form, msg=msg)

    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            msg = '用户名错误'
            return msg
        if not user.password == form.password.data:
            msg = '密码错误'
            return msg
        if user.username == form.username.data and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))

        return render_template('login.html', form=form, msg=msg)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# @app.route('/diary', methods = ['GET'])
# def diary():
#     res = 'test test'
#     return render_template('test.html',res=res)


if __name__ == '__main__':
    app.run()

