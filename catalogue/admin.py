from django.contrib import admin
from .models import Category, Subcategory, Product


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class SubcategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)