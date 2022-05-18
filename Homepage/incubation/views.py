from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IncubationSerializer, IncubationFocalSerializer
from .models import Incubation, IncubationFocal


class IncubationView(viewsets.ModelViewSet):
    """View For Incubational Org"""
    queryset = Incubation.objects.all()
    serializer_class = IncubationSerializer


class IncubationFocalView(viewsets.ModelViewSet):
    """Incubational Focal View"""
    queryset = IncubationFocal.objects.all()
    serializer_class = IncubationFocalSerializer
