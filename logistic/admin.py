from django.contrib import admin

from logistic.models import Product, Stock, StockProduct

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'stocks']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'products',]

@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price',]
