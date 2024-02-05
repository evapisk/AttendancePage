from flask import Blueprint
from models import *


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def main():
    students = Student.query.all()
    return students