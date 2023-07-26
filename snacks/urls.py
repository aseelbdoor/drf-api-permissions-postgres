from django.urls import path
from .views import SnackListView, SnackDetailView

urlpatterns = [
    path('',SnackListView.as_view(),name='List'),
    path('<int:pk>/',SnackDetailView.as_view(),name='details')
]
