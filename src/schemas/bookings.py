from datetime import datetime

from pydantic import BaseModel


class BookingSchema(BaseModel):
    id: int
    date_from: datetime
    date_to: datetime
    user_id: int
