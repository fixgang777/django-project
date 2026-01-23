from django.db import models
from core.models import Product

class Review(models.Model):
    # Делаем привязку к товару необязательной
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        blank=True
    )
    text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв: {self.text[:20]}... ({self.rating}/5)"