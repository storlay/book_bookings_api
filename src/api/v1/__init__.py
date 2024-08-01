from fastapi import APIRouter

from src.api.v1.bookings import router as bookings_router
from src.api.v1.books import router as books_router
from src.api.v1.genres import router as genres_router
from src.api.v1.users import router as users_router
from src.utils.constants import API_V1_PREFIX

routers = (
    bookings_router,
    books_router,
    users_router,
    genres_router,
)

router_v1 = APIRouter(prefix=API_V1_PREFIX)

for router in routers:
    router_v1.include_router(router)
