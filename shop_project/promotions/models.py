from django.db import models
from core.models import Product # Импортируем твои товары

class Promotion(models.Model):
    # Добавляем выбор товара
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='promotions',
        verbose_name="Выберите товар"
    )
    name = models.CharField(max_length=100, verbose_name="Название акции")
    discount_percentage = models.PositiveIntegerField(verbose_name="Процент скидки")
    is_active = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return f"Акция для {self.product.name}: -{self.discount_percentage}%"