from django.urls import path
from django.urls import reverse_lazy
from .views import SnacksListView, SnacksDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    
    path('', SnacksListView.as_view(), name="home"),
    path('<int:pk>/', SnacksDetailView.as_view(), name="snacks_detail"),
    path('create/',SnackCreateView.as_view(),name="Create"),
    path('<int:pk>/update/',SnackUpdateView.as_view(),name="update"),
    path('<int:pk>/delete/',SnackDeleteView.as_view(),name="delete"),

]
