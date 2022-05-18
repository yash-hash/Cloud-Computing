from django.urls import path, include
from rest_framework.routers import DefaultRouter
import event
from event import views

router = DefaultRouter()

router.register('event', views.EventViewSet, basename='event')
router.register('regional', views.RegionalEventViewSet, basename='regional')

urlpatterns = [
    path('', include(router.urls)),
    ]
