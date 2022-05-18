from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ThinkTankSerializer
from .models import ThinkTankProfile

# Create your views here.
class ThinkTankView(viewsets.ModelViewSet):
    """Think Tank View"""
    queryset = ThinkTankProfile.objects.all()
    serializer_class = ThinkTankSerializer
