from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from borrowings.models import Borrowing
from borrowings.serializers import BorrowingListSerializer, BorrowingSerializer


class BorrowingsListView(ModelViewSet):
    queryset = Borrowing.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        else:
            return BorrowingSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Borrowing.objects.all()
        return Borrowing.objects.filter(user=self.request.user)