from django.urls import path, include
from rest_framework import routers
from borrowings.views import BorrowingsListView

app_name = "borrowings"

router = routers.DefaultRouter()
router.register("borrowings", BorrowingsListView)

urlpatterns = [path("", include(router.urls))]