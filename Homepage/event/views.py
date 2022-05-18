from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, RegionalEvent
from .serializers import EventSerializer, RegionalEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Viewset For Event"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RegionalEventViewSet(viewsets.ModelViewSet):
    """Viewset For Regional Event"""
    queryset = RegionalEvent.objects.all()
    serializer_class = RegionalEventSerializer
