from src.models.bookings import Bookings
from src.utils.repository import BaseRepository


class BookingsRepository(BaseRepository):
    model = Bookings
