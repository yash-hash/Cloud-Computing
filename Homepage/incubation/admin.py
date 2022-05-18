from django.contrib import admin
from .models import Incubation, IncubationFocal


@admin.register(IncubationFocal)
class IncubationFocalAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'email', 'designation']

@admin.register(Incubation)
class IncubationAdmin(admin.ModelAdmin):
    list_display = ['incubation_id','name', 'category', 'supported_by', 'country', 'incubation_logo']
