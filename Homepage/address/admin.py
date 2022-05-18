from django.contrib import admin
from .models import Country, State, District, Region

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_id', 'country_name']


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'state_id', 'state_name',]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'district_id', 'district_name',]


@admin.register(Region)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'region_id', 'region_name',]
