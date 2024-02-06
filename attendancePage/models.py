from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Student(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(1000))
    year = db.Column(db.Integer)
    sport = db.Column(db.String(20))
    gender = db.Column(db.String(10))
