from django.urls import path
from .views import SnackListView, SnackDetailView,SnackCreateView

urlpatterns = [
    path('',SnackListView.as_view(),name='List'),
    path('<int:pk>/',SnackDetailView.as_view(),name='details'),
    path('create/',SnackCreateView.as_view(),name='create')
]
