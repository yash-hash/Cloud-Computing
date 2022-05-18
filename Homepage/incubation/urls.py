from django.urls import path, include
from incubation import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('incubation', views.IncubationView, basename = 'incubation')
router.register('focal', views.IncubationFocalView, basename = 'focal')

urlpatterns = [
    path('', include(router.urls)),
]
