from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    # Это разрешает твоему HTML-коду видеть отзывы и отправлять их
    permission_classes = [permissions.AllowAny]