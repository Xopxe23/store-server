from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    product_list = Product.objects.all()
    category_list = ProductCategory.objects.all()
    context = {
        'title': 'Store - Каталог',
        'products': product_list,
        'categories': category_list,
    }
    return render(request, 'products/products.html', context=context)
