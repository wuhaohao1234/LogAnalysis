from flask import Blueprint
from flask_login import current_user

from applications.common import render_template_mixin
from applications.extensions import admin_login_required, db
from applications.models import User
from applications.models.base_model import to_table
from applications.models.loganalysis.task import Task
from applications.models.loganalysis.task_status import TaskStatus
from applications.models.loganalysis.task_type import TaskType
from applications.models.vo.task_list_vo import TaskListVo

bp = Blueprint('task', __name__, url_prefix='/task')


@bp.get('/')
@admin_login_required
def task():
    return render_template_mixin('admin/task_manage.html')


@bp.get('/list')
@admin_login_required
def task_list():
    tasks = db.session.query(Task, TaskType, TaskStatus, User).filter(
        Task.delete_at.is_(None)
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
