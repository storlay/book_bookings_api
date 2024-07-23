from fastapi import FastAPI

from src.api.routers import routers

app = FastAPI(
    title="Book catalog API",
    version="0.1.0",
    root_path="/api"
)

for router in routers:
    app.include_router(router)
