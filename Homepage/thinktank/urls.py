from django.urls import path, include
from thinktank import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('thinkTankProfile', views.ThinkTankView, basename = 'thinkTank')

urlpatterns = [
    path('', include(router.urls)),
]
