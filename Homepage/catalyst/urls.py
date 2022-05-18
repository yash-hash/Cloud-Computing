from django.urls import path, include
from catalyst import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('catalyst', views.CatalystViewSet, basename = 'catalyst')

urlpatterns = [
    path('',include(router.urls))
]
