from django.shortcuts import render
from rest_framework import viewsets
from .models import CarouselImage, SponsorLogo, PartnerLogo, YouthIcon
from .serializers import CarouselImageSerializer, SponsorLogoSerializer, PartnerLogoSerializer, YouthIconSerializer


class CarouselImageView(viewsets.ModelViewSet):
    """View for Carousel Image Model"""
    queryset = CarouselImage.objects.all()
    serializer_class = CarouselImageSerializer


class SponsorLogoView(viewsets.ModelViewSet):
    """View for Sponsor Logo Model"""
    queryset = SponsorLogo.objects.all()
    serializer_class = SponsorLogoSerializer


class PartnerLogoView(viewsets.ModelViewSet):
    """View for PartnerLogo Model"""
    queryset = PartnerLogo.objects.all()
    serializer_class = PartnerLogoSerializer


class YouthIconView(viewsets.ModelViewSet):
    """View for YouthIcon Model"""
    queryset = YouthIcon.objects.all()
    serializer_class = YouthIconSerializer
