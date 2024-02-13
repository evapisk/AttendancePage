from flask import Blueprint, jsonify, render_template

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
def year():
    return render_template(
        'sheets/year.html'
    )

@bp.route('/sport')
def sport():
    return render_template(
        'sheets/sport.html'
    )

@bp.route('/gender')
def gender():
    return render_template(
        'sheets/gender.html'
    )

@bp.route('/6')
def six():
    return render_template(
        'sheets/year/6.html',
        year_list6 = Student.query.all()
    )
@bp.route('/7')
def seven():
    return render_template(
        'sheets/year/7.html',
        year_list7 = Student.query.all()
    )
@bp.route('/8')
def eight():
    return render_template(
        'sheets/year/8.html',
        year_list8 = Student.query.all()
    )

@bp.route('/female')
def female():
    return render_template(
        'sheets/gender/female.html',
        female_list = Student.query.all()
    )

@bp.route('/male')
def male():
    return render_template(
        'sheets/gender/male.html',
        male_list = Student.query.all()
    )

