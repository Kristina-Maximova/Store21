from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')


# def contacts(request):
#     return render(request, 'catalog/contacts.html')


def category(request):
    return render(request, 'catalog/category_1.html')


def orders(request):
    return render(request, 'catalog/orders.html')


def contacts(request):
    if request.method == 'POST':  # POST - словарь с параметрами
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context=context)


def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'catalog/catalog.html', context=context)

def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'catalog/catalog_base.html', context=context)
