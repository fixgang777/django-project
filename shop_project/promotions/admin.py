from django.contrib import admin
from .models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    # Добавляем 'product' в список отображения
    list_display = ('name', 'product', 'discount_percentage', 'is_active')
    list_editable = ('is_active',)