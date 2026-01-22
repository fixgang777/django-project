from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Главная страница магазина
def home_page(request):
    return render(request, 'core/index.html')

# Страница со всеми отзывами
def reviews_page(request):
    return render(request, 'core/reviews.html')

# API для категорий
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# API для продуктов
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer