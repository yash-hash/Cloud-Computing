from rest_framework import serializers
from .models import Institution, InstitutionFocal, InstitutionSponsor

class InstitutionSerializer(serializers.ModelSerializer):
    """Institution Serialiazer"""
    class Meta:
        model = Institution
        fields = "__all__"

class InstitutionFocalSerializer(serializers.ModelSerializer):
    """Institution Focal Serializer"""
    class Meta:
        model = InstitutionFocal
        fields = "__all__"

class InstitutionSponsorSerializer(serializers.ModelSerializer):
    """Institution Sponsor Serializer"""
    class Meta:
        model = InstitutionSponsor
        fields = "__all__"
