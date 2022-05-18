from django.contrib import admin
from .models import Institution, InstitutionFocal, InstitutionSponsor
# Register your models here.

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'institution_name', 'institution_logo']

@admin.register(InstitutionFocal)
class InstitutionFocalAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'email', 'designation']

@admin.register(InstitutionSponsor)
class InstitutionSponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_id', 'contact', 'sponsor_type']
