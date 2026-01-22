from rest_framework import serializers
from .models import Product, Category
from reviews.models import Review  # Импорт для отзывов

# Сериализатор для отзывов
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'text', 'rating', 'created_at']

# Сериализатор для категорий (ЕГО НЕ ХВАТАЛО)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Сериализатор для продуктов
class ProductSerializer(serializers.ModelSerializer):
    # Добавляем отзывы внутрь продукта
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'reviews']