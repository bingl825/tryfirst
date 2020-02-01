from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

@app.route('/')
def home():
    return 'begin'

if __name__ == '__main__':
    app.run()

