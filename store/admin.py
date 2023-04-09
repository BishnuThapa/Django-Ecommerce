from django.contrib import admin
from .models import Product, Variation
# Register your models here.


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category',
                    'created_date', 'updated_date', 'is_available')
    prepopulated_fields = {"slug": ("product_name",)}


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category',
                    'variation_value', 'is_active', 'created_date',)
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
