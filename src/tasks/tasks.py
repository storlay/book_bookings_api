import asyncio

from src.tasks.async_tasks import remove_book_reservation
from src.tasks.celery_conf import celery_app


@celery_app.task(name="remove_book_reservation")
def refresh_car_location_task():
    asyncio.run(remove_book_reservation())
