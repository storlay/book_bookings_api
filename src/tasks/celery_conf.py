import os

from celery import Celery
from celery.schedules import crontab

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

celery_app = Celery(
    "tasks",
    broker=f"redis://{REDIS_HOST}:{REDIS_PORT}",
    include=["src.tasks.tasks"],
)

celery_app.conf.beat_schedule = {
    "refresh_car_location": {
        "task": "remove_book_reservation",
        "schedule": crontab(hour="0", minute="0"),
    }
}
