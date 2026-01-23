from django.contrib import admin
from django.urls import path, include
from core.views import home_page, reviews_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('reviews/', reviews_page, name='reviews_page'),
    # Это подключает API для отзывов:
    path('', include('reviews.urls')),
    # Это подключает API для товаров:
    path('api/shop/', include('core.urls')),
]