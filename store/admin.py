from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'updated_at', 'is_available')
    prepopulated_fields = {'slug': ('name',)}  # Automatically populate the slug field based on the 'name' field
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
