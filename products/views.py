from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None):
    # if category_id:
    #     products = Product.objects.filter(category_id=category_id)
    # else:
    #     products = Product.objects.all()
    # products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
    }
    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
