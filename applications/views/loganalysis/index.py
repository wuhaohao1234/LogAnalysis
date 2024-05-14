from flask import Blueprint

from applications.common import render_template_mixin


bp = Blueprint('index', __name__, url_prefix='/')


@bp.get('/')
@bp.get('/index')
def index():
    return render_template_mixin('loganalysis/index.html')
