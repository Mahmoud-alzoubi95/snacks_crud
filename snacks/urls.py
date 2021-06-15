from django.urls import path

from .views import SnacksListView, SnacksDetailView

urlpatterns = [
    path('', SnacksListView.as_view(), name="snacks_list"),
    path('<int:pk>/', SnacksDetailView.as_view(), name="snacks_detail"),
]