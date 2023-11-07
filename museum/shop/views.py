from django.shortcuts import render, HttpResponseRedirect
from .models import ProductType, Product, ProductBasket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request, category_id=None, page=1):
    per_page = 2
    if category_id:
        category = ProductType.objects.get(id=category_id)
        products = Product.objects.filter(type=category)
        paginator = Paginator(products, per_page)
        products_paginator = paginator.page(page)
    else:
        products = Product.objects.all()
        paginator = Paginator(products, per_page)
        products_paginator = paginator.page(page)
    context = {
        "title": "Магазин",
        "categories": ProductType.objects.all(),
        "products": products_paginator,
    }

    return render(request, "shop/shop.html", context)


def about(request):
    context = {"title": "О магазине"}
    return render(request, "shop/about.html", context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = ProductBasket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        ProductBasket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket_delete(request, basket_id):
    basket = ProductBasket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required
def basket(request):
    context = {
        "title": "Корзина",
        "baskets": ProductBasket.objects.filter(user=request.user),
    }
    return render(request, "shop/basket.html", context)
