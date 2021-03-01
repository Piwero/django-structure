from django.shortcuts import render
from .models import Category, Subcategory, Product


def catalogue(request):
    category = Category.objects.all()
    subcategory = Subcategory.objects.all()
    products = Product.objects.all()

    return render(request, 'catalogue.html', {'category': category, 'subcategory': subcategory, 'products': products})

