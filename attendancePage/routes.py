from flask import Blueprint, jsonify, render_template, request, url_for, redirect

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


bp1 = Blueprint('sheets', __name__, url_prefix='/sheets')
@bp.route('/year')
def year():
    year_list = ['6','7','8']
    return render_template(
        'sheets/year.html',year_list = year_list, year=year
    )

@bp.route('/year/<int:year>')
#creates a route where the year value is inputted based off of list
def year_page(year):
    title = f"{year}th Graders"
    #creates the title of the link on the year page
    return render_template(
        'student_sheet_template.html',
        student_list = db.session.execute(db.select(Student).filter_by(year=year)).scalars(), title = title
        #renders the student sheet template with a year filter
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

@bp.route('/student/add',methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        year = request.form.get('year')
        sport = request.form.get('sport')
        gender = request.form.get('gender')
        schoolId = request.form.get('schoolId')
        student = Student(name=str(fname) + " " + str(lname), year=year, sport=sport, gender=gender, schoolId=schoolId)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main.mainpage'))
    return render_template('main_page.html')

@bp.route('/student/remove',methods=['POST'])
def remove_student():
    print('hi')
    if request.method == 'POST':
        schoolId = request.form.get('schoolId')
        student = Student.query.filter_by(schoolId=schoolId).first()
        print(student)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('main.mainpage'))
    return render_template('main_page.html')


@bp.route('/importdata',methods=['GET'])
def import_data():
    import json
    with open('attendancePage/fakeStudentsForEva.txt') as f:
        student_list = json.load(f)
        print(student_list)

        for student_data in student_list:
            #Accessing attributes in a JSON object using keys
            student = Student(schoolId=student_data['id'], name=student_data['name'], gender=student_data['gender'],
                              sport=student_data['sport'], year=student_data['yearGroup'])

            # Fixed condition checks and appending to lists

            db.session.add(student)
            print(student)

        db.session.commit()
    return redirect(url_for('main.mainpage'))

@bp.route('/attendancemainpage')
def attendance_main():
    return render_template(
        'attendance_page.html',
        student_list=Student.query.all()
    )

@bp.route("/attendanceupdate")
def attendance_update():

    return redirect(url_for('main.mainpage'))
