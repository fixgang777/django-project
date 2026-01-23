from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from reviews.models import Review

# Главная страница
def home_page(request):
    products = Product.objects.all()
    reviews = Review.objects.all().order_by('-created_at')[:3]
    return render(request, 'core/index.html', {
        'products': products,
        'reviews': reviews
    })

# Страница отзывов
def reviews_page(request):
    return render(request, 'core/reviews.html')

# API
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer