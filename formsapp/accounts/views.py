from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request, 'dashboard.html')


def products(request):

    return render(request, 'products.html')


def customer(request):

    return render(request, 'customer.html')

    # return render(request, 'main.html')