from django.shortcuts import render
from .models import Country, State, District, Region
from .serializers import CountrySerializer, StateSerializer, DistrictSerializer, RegionSerializer
from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    """Country viewset"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateViewSet(viewsets.ModelViewSet):
    """State viewset"""
    queryset = State.objects.all()
    serializer_class = StateSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    """District viewset"""
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """Region viewset"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
