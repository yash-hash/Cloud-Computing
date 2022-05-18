from .models import Country, State, District, Region
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    """Country Serializer"""
    class Meta:
        model = Country
        fields = ['country_id', 'country_name',]


class StateSerializer(serializers.ModelSerializer):
    """State Serializer"""
    class Meta:
        model = State
        fields = ['state_id', 'state_name',]


class DistrictSerializer(serializers.ModelSerializer):
    """District Serializer"""
    class Meta:
        model = District
        fields = ['district_id', 'district_name',]


class RegionSerializer(serializers.ModelSerializer):
    """Region Serializer"""
    class Meta:
        model = Region
        fields = ['region_id', 'region_name']
