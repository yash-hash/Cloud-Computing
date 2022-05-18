from rest_framework import serializers
from .models import CarouselImage, SponsorLogo, PartnerLogo, YouthIcon


class CarouselImageSerializer(serializers.ModelSerializer):
    """Carousel Image Serialiazer"""
    class Meta:
        model = CarouselImage
        fields = '__all__'


class SponsorLogoSerializer(serializers.ModelSerializer):
    """Sponsor Logo Serialiazer"""
    class Meta:
        model = SponsorLogo
        fields = '__all__'


class PartnerLogoSerializer(serializers.ModelSerializer):
    """Partner Logo Serialiazer"""
    class Meta:
        model = PartnerLogo
        fields = '__all__'

class YouthIconSerializer(serializers.ModelSerializer):
    """Youth Icon Serialiazer"""
    class Meta:
        model = YouthIcon
        fields = '__all__'
