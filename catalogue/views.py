from django.shortcuts import render
from .models import Category, Product


def catalogue(request):
    category = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'catalogue.html', {'category': category, 'products': products})

