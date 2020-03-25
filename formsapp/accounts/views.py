

from django.shortcuts import render
from .models import Product

def home(request):

    return render(request, 'dashboard.html')


def products(request):
    name=['salom', 'salom2', 'salom3']
    a= Product.objects.filter(name__in=name)
    print(a)
    b = Product.objects.filter(name__iexact=name)
    print(b)
    c= Product.objects.all()
    print(c)
    return render(request, 'products.html')


def customer(request):

    return render(request, 'customer.html')

    # return render(request, 'main.html')