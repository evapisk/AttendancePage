from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def main():
    return "Hello world!"