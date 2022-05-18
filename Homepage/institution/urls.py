from django.urls import path, include
from institution import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('institution', views.InstitutionView, basename = 'institution')
router.register('institution focal', views.InstitutionFocalView, basename = 'institution focal')
router.register('Institution sponsor', views.InstitutionSponsorView, basename = 'Institution sponosr')

urlpatterns = [
    path('', include(router.urls)),
]
