<h1 align="center">API: Сервис бронирования книг 📚</h1>

<div align="center">

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-8B3E2F?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)](http://www.celeryproject.org/)
[![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)](https://python-poetry.org/)


</div>

## Основные возможности

1. **CRUD всех сущностей**
2. **Фильтрация книг по автору, жанрам, стоимости**
3. **Система бронирования книг**
4. **Автоматическое снятие книги с брони при истечении её срока**

## Установка и запуск

1. Склонируйте репозиторий:

```
git clone https://github.com/storlay/book_bookings_api.git
```

2. В корне создайте и заполните файл `.env`


3. Запустите проект с помощью Docker Compose:

```
docker compose -f infra/docker-compose.yml up --build
```

4. Приложение будет доступно по адресу http://127.0.0.1:8000

## Использование

- **Документация API** доступна по адресам:
    - http://127.0.0.1:8000/docs (Swagger)
    - http://127.0.0.1:8000/redoc (Redoc)

- **Мониторинг и управление фоновыми задачами** доступны по адресу:
    - http://127.0.0.1:5555 (Flower)