from rest_framework import serializers
from .models import ThinkTankProfile

class ThinkTankSerializer(serializers.ModelSerializer):
    """Think Tank  Serializer"""

    class Meta:
        model = ThinkTankProfile
        fields = '__all__'
