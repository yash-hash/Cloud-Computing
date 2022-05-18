from django.shortcuts import render
from rest_framework import viewsets
from .models import Champion
from .serializers import ChampionSerializer


class ChampionView(viewsets.ModelViewSet):
    """View for Champion Model"""
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
