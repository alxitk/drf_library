from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from books.models import Book
from borrowings.models import Borrowing

BORROWING_URL = reverse("borrowings:borrowing-list")

class UnauthenticatedBorrowingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        response = self.client.get(BORROWING_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedBorrowingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = get_user_model().objects.create_user(
            email="<EMAIL>",
            password="<PASSWORD>",
        )
        self.user2 = get_user_model().objects.create_user(
            email="<EMAIL_2>",
            password="<PASSWORD>",
        )
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            cover="Harfd",
            inventory=3,
            daily_fee=10.10,
        )

    def test_user_sees_only_own_borrowings(self):
        Borrowing.objects.create(
            borrow_date = "2025-10-01",
            expected_return_date = "2025-10-10",
            book = self.book,
            user = self.user1,
        )
        Borrowing.objects.create(
            borrow_date = "2025-10-01",
            expected_return_date = "2025-10-10",
            book = self.book,
            user = self.user2,
        )
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(BORROWING_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

