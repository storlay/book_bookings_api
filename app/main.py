from fastapi import FastAPI

app = FastAPI(
    title="Book catalog API",
    version="0.1.0",
    root_path="/api"
)
