from flask import Blueprint, jsonify
from .models import Student


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def main():
    output = ""
    for u in Student.query.all():
        output += str(u.__dict__) + "\n"
    return output