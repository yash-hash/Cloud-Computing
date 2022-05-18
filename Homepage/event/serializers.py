from rest_framework import serializers
from .models import Event, RegionalEvent


class EventSerializer(serializers.ModelSerializer):
    """Serialiazer for Event"""
    class Meta:
        model = Event
        fields = '__all__'


class RegionalEventSerializer(serializers.ModelSerializer):
    """Serialiazer for Regional Event"""
    class Meta:
        model = RegionalEvent
        fields = '__all__'
