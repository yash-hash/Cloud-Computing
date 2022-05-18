from rest_framework import serializers
from .models import Catalyst


class CatalystSerializer(serializers.ModelSerializer):
    """Catalyst Serialiazer"""
    class Meta:
        model = Catalyst
        fields = '__all__'
