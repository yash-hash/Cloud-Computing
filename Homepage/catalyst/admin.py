from django.contrib import admin
from .models import Catalyst


@admin.register(Catalyst)
class CatalystAdmin(admin.ModelAdmin):
    """Catalyst Admin"""
    list_display = ['catalyst_id', 'first_name', 'last_name', 'email_id']
