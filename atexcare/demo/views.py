from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    context = {}
    return render(request, 'demo/index.html', context)


def products(request):
    lista = Product.objects.all()
    context = {
        "productos": lista,
    }
    return render(request, 'demo/products.html', context)


def product(request, pk):
    instance = Product.objects.get(id=pk)
    # Obtener de many to many
    a = Feature.objects.filter(product=pk)
    context = {'producto': instance,
    'caracteristicas': a}
    return render(request, 'demo/product.html', context)


def who(request):
    context = {}
    return render(request, 'demo/who.html', context)


def legal(request):
    context = {}
    return render(request, 'demo/legal.html', context)


def contact_info(request):
    context = {}
    return render(request, 'demo/contact_info.html', context)


def detail_car(request):
    context = {}
    return render(request, 'demo/detail_car.html', context)


def sending_info(request):
    context = {}
    return render(request, 'demo/sending_info.html', context)


def login(request):
    context = {}
    return render(request, 'demo/login.html', context)


def register(request):
    context = {}
    return render(request, 'demo/register.html', context)


def user(request):
    context = {}
    return render(request, 'demo/user.html', context)
