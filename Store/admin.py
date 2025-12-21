from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']


from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
