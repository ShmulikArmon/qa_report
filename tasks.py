from celery import Celery
from populatedb import populate_call
from celery.utils.log import get_task_logger
from django.core.cache import cache

logger = get_task_logger(__name__)

LOCK_EXPIRE = 60 * 5 # Lock expires in 5 minutes


app = Celery('tasks', broker="amqp://guest@localhost//")
app.config_from_object('celeryconfig')

@app.task
def test():
    print "task has been activated"

@app.task
def populate_db():
    populate_call()

@app.task
def locked_populate():
    lock_id = "something unique"
    lock_expire = 60 * 5  # five minutes

    acquire_lock = lambda: cache.add(lock_id, "true", lock_expire)
    release_lock = lambda: cache.delete(lock_id)

    if acquire_lock():
        try:
            populate_call()
        finally:
            release_lock()