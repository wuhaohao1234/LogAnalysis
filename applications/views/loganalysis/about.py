from flask import Blueprint

from applications.common import render_template_mixin

bp = Blueprint('about', __name__, url_prefix='/about')


@bp.route('/')
def about():
    return render_template_mixin('loganalysis/about.html')
