from django.contrib import admin
from .models import Event,RegionalEvent

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin Model For Event"""
    list_display = ['event_id', 'name', 'date', 'type', 'description']


@admin.register(RegionalEvent)
class RegionalEvent(admin.ModelAdmin):
    """Admin Model for Regional Event"""
    list_display = ['id', 'name', 'date', 'type', 'description']
