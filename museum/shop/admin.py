from django.contrib import admin
from .models import ProductType, Product, ProductBasket
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductBasket)