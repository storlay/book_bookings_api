from src.api.books import router as books_router
from src.api.genres import router as genres_router
from src.api.users import router as users_router

routers = (
    books_router,
    users_router,
    genres_router,
)
