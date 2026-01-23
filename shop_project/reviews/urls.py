from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet

router = DefaultRouter()
# Твой фронтенд на скрине ищет эндпоинт /api/reviews/list/
router.register(r'list', ReviewViewSet, basename='review-api')

urlpatterns = [
    path('api/reviews/', include(router.urls)),
]