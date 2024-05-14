import os
from datetime import datetime

import requests
from flask import Blueprint, request, current_app
from flask_login import current_user
from sqlalchemy import and_
from werkzeug.utils import secure_filename

from applications.common import render_template_mixin
from applications.common.utils.http import success_api, fail_api
from applications.extensions import user_login_required, db
from applications.models import User
from applications.models.base_model import to_table
from applications.models.loganalysis.task import Task
from applications.models.vo.task_list_vo import TaskListVo
from applications.models.loganalysis.task_report import TaskReport
from applications.models.loganalysis.task_status import TaskStatus
from applications.models.loganalysis.task_type import TaskType
from applications.views.loganalysis.message import send_message

bp = Blueprint('task', __name__, url_prefix='/task')


@bp.get('/')
@user_login_required
def task():
    return render_template_mixin('loganalysis/task.html')


@bp.post('/add')
@user_login_required
def add_task():
    rq = request.form
    url = rq.get('url')
    task_type_id = rq.get('task_type_id')
    task = Task(uid=current_user.id, url=url, task_type_id=task_type_id)
    db.session.add(task)
    db.session.commit()
    send_message(1, current_user.id, '任务添加成功')
    start_scan(uid=current_user.id, task_id=task.id, url=url)

    return success_api('任务添加成功')


@bp.get('/delete')
@user_login_required
def delete_task():
    task_id = request.args.get('id')

    task = Task.query.get(task_id)
    if task is None:
        return fail_api('删除失败')
    if task.uid != current_user.id:
        return fail_api('您无权删除此任务')

    task.delete_at = datetime.now()
    db.session.commit()

    report = TaskReport.query.filter(TaskReport.scan_id == task_id).first()
    if report is not None:
        report.delete_at = datetime.now()
        db.session.commit()

    return success_api('删除成功')

def start_scan(uid, task_id, url):
    scan_api_url = current_app.config['SCAN_API_URL']
    add_report_url = current_app.config['ADD_REPORT_URL']
    r = requests.get(scan_api_url, params={'uid': uid, 'task_id': task_id, 'url': url, 'api': add_report_url})


@bp.post('/add_report')
# @user_login_required
def add_report():
    uid = request.form.get('uid')
    task_id = request.form.get('task_id')
    task_status_id = request.form.get('task_status_id')
    report_file = request.files.getlist('report_file')
    if (uid is None or task_id is None or task_status_id is None
            or int(task_status_id) not in [2, 3] or (int(task_status_id) == 2 and report_file is None)):
        return fail_api('参数错误')
    task = Task.query.get(int(task_id))
    if task is None:
        return fail_api('任务不存在')
    task.task_status_id = task_status_id
    task.update_at = datetime.now()
    db.session.commit()

    msg = '任务更新成功'
    if int(task_status_id) == 2:
        report_file = request.files.get('report_file')
        report_name = secure_filename(report_file.filename)
        upload_path = current_app.config['REPORT_UPLOAD_FOLDER']
        report_path = os.path.join(upload_path, report_name)
        report_file.save(report_path)
        report = TaskReport(task_id, report_path=report_path)
        db.session.add(report)
        db.session.commit()

        msg = '报告上传成功'
    send_message(1, uid, '任务完成')
    return success_api(msg=msg)


@bp.get('/mine')
@user_login_required
def mine_task():
    return render_template_mixin('loganalysis/mine_task.html')

@bp.get('/list')
@user_login_required
def task_list():
    tasks = db.session.query(Task, TaskType, TaskStatus, User).filter(
        and_(Task.delete_at.is_(None), Task.uid == current_user.id)
    ).join(
        TaskType,
        Task.task_type_id == TaskType.id
    ).join(
        TaskStatus,
        Task.task_status_id == TaskStatus.id
    ).join(
        User,
        Task.uid == User.id
    ).order_by(Task.create_at.desc())

    t_list = []
    for task, task_type, task_status, user in tasks:
        t_list.append(
            TaskListVo(
                id=task.id,
                username=user.username,
                url=task.url,
                task_type=task_type.type,
                task_status=task_status.status,
                create_at=task.create_at,
                update_at=task.update_at
            )
        )
    return to_table(t_list)


@bp.get('/newstart_list')
def newstart_task_list():
    tasks = db.session.query(Task, TaskType, TaskStatus, User).filter(
        and_(Task.delete_at.is_(None), Task.task_type_id == 1)
    ).join(
        TaskType,
        Task.task_type_id == TaskType.id
    ).join(
        TaskStatus,
        Task.task_status_id == TaskStatus.id
    ).join(
        User,
        Task.uid == User.id
    ).order_by(Task.create_at.desc()
               ).limit(10)

    t_list = []
    for task, task_type, task_status, user in tasks:
        t_list.append(
            TaskListVo(
                id=task.id,
                username=user.username,
                url=task.url,
                task_type=task_type.type,
                task_status=task_status.status,
                create_at=task.create_at,
                update_at=task.update_at
            )
        )
    return to_table(t_list)


@bp.get('/newdone_list')
def newdone_task_list():
    task_id = request.args.get('id')
    if task_id is None:
        tasks = db.session.query(Task, TaskType, TaskStatus, User).filter(
            and_(Task.delete_at.is_(None), Task.task_type_id == 1, Task.task_status_id == 2)
        ).join(
            TaskType,
            Task.task_type_id == TaskType.id
        ).join(
            TaskStatus,
            Task.task_status_id == TaskStatus.id
        ).join(
            User,
            Task.uid == User.id
        ).order_by(Task.update_at.desc()
                   ).limit(10)
    else:
        tasks = db.session.query(Task, TaskType, TaskStatus, User).filter(
            and_(Task.delete_at.is_(None),Task.task_type_id == 1, Task.task_status_id == 2, Task.id == task_id)
        ).join(
            TaskType,
            Task.task_type_id == TaskType.id
        ).join(
            TaskStatus,
            Task.task_status_id == TaskStatus.id
        ).join(
            User,
            Task.uid == User.id
        ).order_by(Task.update_at.desc())

    t_list = []
    for task, task_type, task_status, user in tasks:
        t_list.append(
            TaskListVo(
                id=task.id,
                username=user.username,
                url=task.url,
                task_type=task_type.type,
                task_status=task_status.status,
                create_at=task.create_at,
                update_at=task.update_at
            )
        )
    return to_table(t_list)