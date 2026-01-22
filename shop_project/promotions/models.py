from django.db import models
from core.models import Product

class Promotion(models.Model):
    product = models.ForeignKey(Product, related_name='promotions', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    discount_percentage = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.discount_percentage}% off on {self.product.name}"