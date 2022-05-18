from rest_framework import serializers
from .models import Champion


class ChampionSerializer(serializers.ModelSerializer):
    """Champion Serialiazer"""
    # contact_one = serializers.CharField(max_length=10, validators=[phone_val])
    class Meta:
        model = Champion
        fields = "__all__"
        
