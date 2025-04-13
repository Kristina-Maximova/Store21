from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'catalog/home.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def category(request):
    return render(request, 'catalog/category_1.html')


def orders(request):
    return render(request, 'catalog/orders.html')


def contact(request):
    if request.method == 'POST':  # POST - словарь с параметрами
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'catalog/contacts.html')
