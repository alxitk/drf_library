from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from books.models import Book
from users.models import User

BOOKS_URL = reverse("books:book-list")

class BooksApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title="Book 1",
            author="<NAME>",
            cover="Hard",
            inventory=10,
            daily_fee=5.0
        )
        self.user = User.objects.create_user(
            email="<EMAIL>",
            password="<PASSWORD>",
        )

    def test_create_book_forbidden(self):
        payload = {
            "title": "test book",
            "author": "test author",
            "cover": "Hard",
            "inventory": 10,
            "daily_fee": 5.0
        }
        self.client.force_authenticate(user=self.user)

        response = self.client.post(BOOKS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_book_str_returns_title(self):
        self.assertEqual(str(self.book), self.book.title)

    def test_anyone_can_list_books_and_data_in_response(self):
        response = self.client.get(BOOKS_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.count())
        self.assertEqual(response.data[0]["title"], self.book.title)
        self.assertEqual(response.data[0]["author"], self.book.author)
        self.assertEqual(response.data[0]["cover"], self.book.cover)
        self.assertEqual(response.data[0]["inventory"], self.book.inventory)
        self.assertEqual(float(response.data[0]["daily_fee"]), float(self.book.daily_fee))




