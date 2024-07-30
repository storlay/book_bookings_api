import datetime

from src.utils.transaction import TransactionManager


async def remove_book_reservation() -> None:
    """
    The logic of deleting expiring bookings.
    :return: None.
    """
    current_date = datetime.date.today()
    async with TransactionManager() as transaction:
        await transaction.bookings_repo.remove_old_bookings(
            current_date,
        )
        await transaction.commit()
