from django.urls import path

from .views import SnacksListView, SnacksDetailView, SnackCreateView

urlpatterns = [
    path('', SnacksListView.as_view(), name="home"),
    path('<int:pk>/', SnacksDetailView.as_view(), name="snacks_detail"),
    path('create/',SnackCreateView.as_view(),name="Create")
]
