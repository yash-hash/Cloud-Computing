from django.urls import path, include
import address
from address import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('country', views.CountryViewSet, basename = 'country')
router.register('state', views.StateViewSet, basename = 'state')
router.register('district', views.DistrictViewSet, basename = 'district')
router.register('region', views.RegionViewSet, basename = 'region')

urlpatterns = [
    path('', include(router.urls)),
]
