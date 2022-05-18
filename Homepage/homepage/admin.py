from django.contrib import admin
from .models import CarouselImage, SponsorLogo, PartnerLogo, YouthIcon


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_id', 'image_event_name', 'image_file','date_added']


@admin.register(SponsorLogo)
class SponsorLogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_id', 'sponsor_name', 'sponsor_desc', 'image_file', 'sponsor_type','date_added']


@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_id', 'partner_name', 'partner_desc', 'image_file', 'partner_type','date_added']


@admin.register(YouthIcon)
class YouthIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'image_id', 'image_file', 'designation', 'date_added']
