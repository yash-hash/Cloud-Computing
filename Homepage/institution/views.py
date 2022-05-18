from django.shortcuts import render
from rest_framework import viewsets
from .models import Institution, InstitutionFocal, InstitutionSponsor
from .serializers import InstitutionSerializer, InstitutionFocalSerializer, InstitutionSponsorSerializer
# Create your views here.

class InstitutionView(viewsets.ModelViewSet):
    """View for Institution Model"""
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class InstitutionFocalView(viewsets.ModelViewSet):
    """View for Institution Focal"""
    queryset = InstitutionFocal.objects.all()
    serializer_class = InstitutionFocalSerializer


class InstitutionSponsorView(viewsets.ModelViewSet):
    """ View For Institution Sponsor """
    queryset = InstitutionSponsor.objects.all()
    serializer_class = InstitutionSponsorSerializer
