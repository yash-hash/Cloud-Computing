from django.shortcuts import render
from rest_framework import viewsets
from .models import Catalyst
from .serializers import CatalystSerializer


class CatalystViewSet(viewsets.ModelViewSet):
    """Catalyst ViewSet"""
    queryset = Catalyst.objects.all()
    serializer_class = CatalystSerializer
