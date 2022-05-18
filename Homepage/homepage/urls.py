from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import homepage
from homepage import views

router = DefaultRouter()

router.register('carousel', homepage.views.CarouselImageView, basename = 'carousel'),
router.register('sponsor', homepage.views.SponsorLogoView, basename = 'sponsor'),
router.register('youthicon', homepage.views.YouthIconView, basename = 'youthicon'),
router.register('partner', homepage.views.PartnerLogoView, basename = 'partner'),

urlpatterns = [
    path('', include(router.urls)),
    ]
