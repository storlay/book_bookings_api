from fastapi import FastAPI

from src.api.v1 import router_v1

app = FastAPI(
    title="Book catalog API",
    version="0.1.0",
    root_path="/api",
)

app.include_router(router_v1)
