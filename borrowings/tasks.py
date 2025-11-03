from django.utils import timezone

from borrowings.models import Borrowing
from notifications.utils import send_telegram_message


def check_overdue_borrowings():
    today = timezone.now().date()
    overdue_borrowings = Borrowing.objects.filter(
        expected_return_date__lte=today,
        actual_return_date__isnull=True,
    )

    if not overdue_borrowings.exists():
        send_telegram_message(
            "No borrowings overdue today"
        )
        return

    for b in overdue_borrowings:
        message = (
            f"Overdue borrowing:\n"
            f"Book: {b.book.title}\n"
            f"User: {b.user.email}\n"
            f"Expected return date: {b.expected_return_date}"
        )
        send_telegram_message(message)