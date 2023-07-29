from django.urls import path
from .views import SnackHomeView

urlpatterns = [
    path('',SnackHomeView.as_view(),name='home')
]
