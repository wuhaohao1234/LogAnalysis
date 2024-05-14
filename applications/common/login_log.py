from flask_login import current_user

from applications.common.utils.validate import str_escape
from applications.extensions import db
from applications.models import LoginLog, BaseModel


def login_log(request, uid, is_access):
    role = ''
    if current_user.is_authenticated:
        role = f'/{current_user.role}'
    info = {
        'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': str_escape(request.headers.get('User-Agent')),
        'description': str_escape(f"{request.form.get('username')}{role}"),
        'uid': uid,
        'success': int(is_access)
    }

    log = LoginLog.from_dict(LoginLog, info)
    db.session.add(log)
    db.session.flush()
    db.session.commit()
    return log.id


def admin_log(request, is_access):
    request_data = request.json if request.headers.get('Content-Type') == 'application/json' else request.values
    info = {
        # 'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': str_escape(request.headers.get('User-Agent')),
        # 'desc': str_escape(str(dict(request_data))),
        'uid': current_user.id,
        'success': int(is_access)

    }
    log = LoginLog.from_dict(info)
    db.session.add(log)
    db.session.commit()

    return log.id
