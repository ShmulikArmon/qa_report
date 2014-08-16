from datetime import timedelta

CELERY_IMPORTS=("tasks",)

CELERYBEAT_SCHEDULE = {
    'populate-every-60-seconds': {
        'task': 'tasks.locked_populate',
        'schedule': timedelta(seconds=60)
    },
}

CELERY_TIMEZONE = 'UTC'