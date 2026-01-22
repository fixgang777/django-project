from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views as core_views  # Импортируем модуль views под псевдонимом

urlpatterns = [
    # Теперь мы ОБЯЗАТЕЛЬНО пишем core_views. перед названием функции
    path('', core_views.home_page, name='home'),
    path('reviews-list/', core_views.reviews_page, name='reviews_page'),
    path('admin/', admin.site.urls),
    path('api/shop/', include('core.urls')),
]

# Проверка дополнительных модулей
if getattr(settings, 'ENABLE_REVIEWS', False):
    urlpatterns.append(path('api/reviews/', include('reviews.urls')))

if getattr(settings, 'ENABLE_PROMOTIONS', False):
    urlpatterns.append(path('api/promotions/', include('promotions.urls')))