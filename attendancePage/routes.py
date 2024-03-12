from flask import Blueprint, jsonify, render_template, request

from . import db
from .auth import unauthorized
from .models import Student


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def main():
    return render_template(
        'index.html'
    )

@bp.route('/database')
def database():
    output = ""
    for u in Student.query.all():
        output += str(u.__dict__) + "\n"
    return output

@bp.route('/master')
def mainpage():
    return render_template(
        'main_page.html',
        student_list=Student.query.all()
    )

@bp.route('/indv')
def indv():
    print("hello")
    return render_template(
        'indv.html'
    )
@bp.route('/admin')
def admin():
    return render_template(
        'admin.html'
    )


bp1 = Blueprint('sheets', __name__, url_prefix='/sheets')
@bp.route('/year')
def yearsheet():
    return render_template(
        'sheets/year.html'
    )

@bp.route('/year/<int:year>')
def year(year):
    title = f"{year}th Graders"
    return render_template(
        'student_sheet_template.html',
        student_list = db.session.execute(db.select(Student).filter_by(year=year)).scalars(), title = title
    )

@bp.route('/sport')
def sport():
    sport_list = ['football','lacrosse','volleyball','basketball','swimming','soccer']
    return render_template(
        'sheets/sport.html',sport_list=sport_list
    )

@bp.route('/sport/<string:sport>')
def sport_page(sport):
    title = f"{sport.capitalize()} Players"
    return render_template(
        'student_sheet_template.html',student_list = db.session.execute(db.select(Student).filter_by(sport=sport)).scalars(), sport = sport, title = title
    )

@bp.route('/gender')
def gender():
    gender_list = ['male','female']
    return render_template(
        'sheets/gender.html', gender_list=gender_list, gender=gender
    )

@bp.route('/gender/<string:gender>')
def gender_page(gender):
    title = f"{gender.capitalize()}s"
    return render_template(
        'student_sheet_template.html',student_list = db.session.execute(db.select(Student).filter_by(gender=gender[0].capitalize())).scalars(), gender = gender, title = title
    )

@bp.route('/addstudent',methods=['POST'])
def add_student():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        year = request.form.get('year')
        sport = request.form.get('sport')
        gender = request.form.get('gender')
        schoolid = request.form.get('schoolid')
        student = Student(name=fname + " " + lname, year=year, sport=sport, gender=gender, schoolId=schoolid)
    return render_template(
        'main_page.html'
    )