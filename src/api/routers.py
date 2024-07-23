from src.api.genres import router as genres_router
from src.api.users import router as users_router

routers = (
    users_router,
    genres_router,
)
