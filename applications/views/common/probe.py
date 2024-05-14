from flask import Blueprint, send_file, make_response, send_from_directory

bp = Blueprint('probe', __name__, url_prefix='/')


@bp.route('/probe.py')
def download_probe():
    # directory = os.getcwd()  # 假设在当前目录
    # response = make_response(send_from_directory('probe', 'probe.py', as_attachment=True))
    # response.headers["Content-Disposition"] = "attachment; filename={}".format('probe.py')
    #
    # return response
    return send_file('probe/probe.py', download_name='probe.py', mimetype='application/json', as_attachment=True)
