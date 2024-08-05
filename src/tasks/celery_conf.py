from celery import Celery
from celery.schedules import crontab

from src.config.config import settings


celery_app = Celery(
    "tasks",
    broker=f"redis://{settings.redis.HOST}:{settings.redis.PORT}",
    include=["src.tasks.tasks"],
)

celery_app.conf.beat_schedule = {
    "refresh_car_location": {
        "task": "remove_book_reservation",
        "schedule": crontab(hour="0", minute="0"),
    }
}
