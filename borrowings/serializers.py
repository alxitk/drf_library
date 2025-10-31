from rest_framework import serializers
from django.utils import timezone

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


class CreateBorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ("id", "book", "expected_return_date",)

    def create(self, validated_data):
        book = validated_data.pop("book")
        user = self.context['request'].user

        if book.inventory <= 0:
            raise serializers.ValidationError("Book is out of stock")

        book.inventory -= 1
        book.save()

        borrowing = Borrowing.objects.create(
            user=user,
            book=book,
            borrow_date=timezone.now().date(),
            expected_return_date=validated_data["expected_return_date"],
        )

        return borrowing