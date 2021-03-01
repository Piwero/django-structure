from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.title


class Supplier(models.Model):
    pass


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    reference = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=150, unique=True)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="products")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
