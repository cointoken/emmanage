from datetime import timedelta
from celery.schedule import crontab


BROKER_URL = 'redis://127.0.0.1:6379' 
CELERY_TIMEZONE='Asia/Shanghai' 

CELERY_IMPORTS = (                                  
    'tasks.task'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'tasks.task.datas_get',
         'schedule': timedelta(seconds=30),       # 每 30 秒执行一次
         'args': () 
    }                                             # 任务函数参数
    # },
    # 'multiply-at-some-time': {
    #     'task': 'celery_app.task2.multiply',
    #     'schedule': crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
    #     'args': (3, 7)                            # 任务函数参数
    # }
}

#celery -B -A tasks worker --loglevel=info