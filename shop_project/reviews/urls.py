from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

# Создаем роутер для автоматической генерации путей API
router = DefaultRouter()
# Теперь отзывы будут доступны по адресу: /api/reviews/list/
router.register(r'list', ReviewViewSet, basename='review')

urlpatterns = [
    # Подключаем все маршруты роутера
    path('', include(router.urls)),
]