from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import Snack
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer
from rest_framework.permissions import AllowAny

class SnackListView(ListCreateAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer
    from rest_framework.permissions import AllowAny

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Snack.objects.all()
    serializer_class=SnackSerializer