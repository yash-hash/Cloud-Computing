from django.urls import path, include
from quiz import views
from rest_framework.routers import DefaultRouter

"""
router = DefaultRouter()
router.register('quiz', views.QuizViewSet, basename = 'quiz')
urlpatterns = [
    path('', include(router.urls)),
]"""

urlpatterns = [
    path('list_category', views.ListCategories.as_view()),
    path('start/', views.StartQuiz.as_view()),
    path('start/<int:category_id>/', views.StartQuiz.as_view()),
]
