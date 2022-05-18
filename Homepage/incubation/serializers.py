from rest_framework import serializers
from .models import Incubation, IncubationFocal


class IncubationFocalSerializer(serializers.ModelSerializer):
    """Incubation Focal Serializer"""
    class Meta:
        model = IncubationFocal
        fields = '__all__'


class IncubationSerializer(serializers.ModelSerializer):
    """Incubation  Serializer"""

    class Meta:
        model = Incubation
        fields = '__all__'
