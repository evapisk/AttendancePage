from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

from . import db
from flask_login import UserMixin
import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    schoolId = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    year = db.Column(db.Integer)
    sport = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    attendance_status = db.Column(db.String(10))  # This field stores the attendance status

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    status = db.Column(db.String(10))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", backref=backref("student", uselist=False))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<Student {}>'.format(self.name)


