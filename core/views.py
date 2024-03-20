from multiprocessing import context
from django.shortcuts import render
from .models import Products, Doctors
# Create your views here.

def home(request):
    product = Products.objects.all()
    doctor = Doctors.objects.all()
    context = {

        'product': product,
        'doctor': doctor

    }

    return render (request, 'index.html', context)

def doctor(request):
    doctor = Doctors.objects.all()
    context = {

        'doctor': doctor
    }
    return render (request, 'doctors.html', context)

def cart(request):
    return render (request, 'carts.html')

def product(request):
    product = Products.objects.all()
    context = {

        'product': product
    }
    return render(request, 'product.html', context)