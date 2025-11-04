from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from borrowings.models import Borrowing
from borrowings.serializers import (
    BorrowingListSerializer,
    BorrowingSerializer,
    CreateBorrowingSerializer,
)


class BorrowingsView(ModelViewSet):
    queryset = Borrowing.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        elif self.action == "create":
            return CreateBorrowingSerializer
        return BorrowingSerializer

    def get_queryset(self):
        queryset = Borrowing.objects.all()
        user = self.request.user

        if not user.is_staff:
            queryset = queryset.filter(user=user)
        else:
            user_id = self.request.query_params.get("user_id")
            if user_id:
                queryset = queryset.filter(user_id=user_id)

        is_active = self.request.query_params.get("is_active")
        if is_active:
            if is_active.lower() == "true":
                queryset = queryset.filter(actual_return_date__isnull=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(actual_return_date__isnull=False)

        return queryset

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def return_borrowing(self, request, *args, **kwargs):
        borrowing = self.get_object()
        if borrowing.actual_return_date:
            return Response(
                {"error": "This borrowing has already been returned."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        borrowing.actual_return_date = timezone.now().date()

        borrowing.book.inventory += 1
        borrowing.book.save()
        borrowing.save()

        return Response(
            {"message": "Book returned successfully."},
            status=status.HTTP_200_OK,
        )
