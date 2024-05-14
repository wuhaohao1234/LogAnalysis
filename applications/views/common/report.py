from flask import Blueprint, request

from applications.common import render_template_mixin
from applications.models.loganalysis.task_report import TaskReport

bp = Blueprint('report', __name__, url_prefix='/report')


@bp.route('/', methods=['GET', 'POST'])
def get_report():
    report = TaskReport.query.filter(TaskReport.scan_id == request.args['task_id']).first()
    return render_template_mixin('common/report.html', opt=report)
