from datetime import timedelta

BROKER_URL = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds':{
        'tasks': 'tasks.datas_get',
        'schedule': timedelta(hours=2),
        'args': ()
    }
}

#python xx.py celery worker --logevel=info --beat
#python xx.py celery beat --logevel=info

# celery 