from multiprocessing import context
from django.shortcuts import render
from .models import Products
# Create your views here.

def home(request):
    product = Products.objects.all()
    context = {
        'product': product,
    }

    return render (request, 'index.html', context)


def cart(request):
    return render (request, 'carts.html')

def product(request):
    product = Products.objects.all()
    context = {

        'product': product
    }
    return render(request, 'product.html', context)