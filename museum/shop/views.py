from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Магазин'}
    return render(request, 'shop/shop.html', context)

def about(request):
    context = {
        'title': 'О магазине'
    }
    return render(request, 'shop/about.html', context)