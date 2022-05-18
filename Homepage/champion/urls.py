from django.urls import path, include
from champion import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('champion', views.ChampionView, basename = 'champion')

urlpatterns = [
    path('', include(router.urls)),
]
