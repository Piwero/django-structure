from django.shortcuts import render
from .models import Category, Subcategory, Product


def catalogue(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products = Product.objects.all()

    return render(request, 'catalogue2.html', {'categories': categories, 'subcategories': subcategories, 'products': products})

