from rest_framework.viewsets import ModelViewSet

from borrowings.models import Borrowing
from borrowings.serializers import BorrowingListSerializer, BorrowingSerializer


class BorrowingsListView(ModelViewSet):
    queryset = Borrowing.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BorrowingListSerializer
        else:
            return BorrowingSerializer
