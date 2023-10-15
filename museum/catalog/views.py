from django.shortcuts import render, HttpResponseRedirect
from .models import Exhibition, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def about(request):
    return render(request, 'catalog/about.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def exhibition(request, page=1):
    #type_id = 1 -> Выставка
    exhibitions = Exhibition.objects.filter(type_id=1)
    per_page = 2
    paginator = Paginator(exhibitions, per_page)
    exhibition_paginator = paginator.page(page)

    context = {
        'title': 'Выставки',
        'exhibitions': exhibition_paginator,
    }
    return render(request, 'catalog/exhibition.html', context)

def events(request, page=1):
    #type_id = 2 -> Событие
    events = Exhibition.objects.filter(type_id=2)
    per_page = 2
    paginator = Paginator(events, per_page)
    events_paginator = paginator.page(page)

    context = {
        'title': 'События',
        'events': events_paginator,
    }
    return render(request, 'catalog/events.html', context)

@login_required
def basket_add(request, exhibition_id):
    exhibition = Exhibition.objects.get(id=exhibition_id)
    baskets = Basket.objects.filter(user=request.user, exhibition=exhibition)

    if not baskets.exists():
        Basket.objects.create(user=request.user, exhibition=exhibition, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])    