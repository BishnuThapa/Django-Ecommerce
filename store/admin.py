from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category',
                    'created_date', 'updated_date', 'is_available')
    prepopulated_fields = {"slug": ("product_name",)}
