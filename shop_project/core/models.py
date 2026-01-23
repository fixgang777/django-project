from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    @property
    def discount_price(self):
        # Импорт внутри метода, чтобы избежать круговой ошибки
        from promotions.models import Promotion
        promo = Promotion.objects.filter(product=self).first()
        if promo:
            # Считаем новую цену: цена - процент
            return float(self.price) * (1 - promo.discount_percentage / 100)
        return None

    def __str__(self): return self.name