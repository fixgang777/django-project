from rest_framework import viewsets, serializers, permissions
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # Позволяет любому пользователю просматривать и добавлять отзывы
    permission_classes = [permissions.AllowAny]