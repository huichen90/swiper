import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tantan.settings')

# TODO
# 1. 发送手机验证码
# 2. 上传头像到七牛云
# 3. 登录后自动加载数据到 redis
# 4. 存储处理

celery_app = Celery('tantan')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()


def worker_task_call(func):
    '''将任务异步化执行'''
    task = celery_app.task(func)
    return task.delay
