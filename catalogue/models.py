from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    subcategory = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Supplier(models.Model):
    pass


class Product(models.Model):
    active = models.BooleanField(default=True)
    reference = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="products")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
