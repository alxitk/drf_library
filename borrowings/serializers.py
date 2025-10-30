from rest_framework import serializers

from books.models import Book
from books.serializers import BookSerializer
from borrowings.models import Borrowing


class BorrowingListSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = ("id", "borrow_date", "book", "expected_return_date", "actual_return_date", "user")


class BorrowingSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Borrowing
        fields = ("id", "book", "expected_return_date", "actual_return_date", "user")