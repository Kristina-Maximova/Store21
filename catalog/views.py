from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Product, Category


# Create your views here.
# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'catalog/home.html', context=context)


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)  # 3 элемента на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/home.html', {'page_obj': page_obj})


def catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'catalog/catalog.html', context=context)


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

def user_add_product(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image") # так сюда передается файл
        price = request.POST.get("price")
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        new_product = Product.objects.create(
            name=name,
            description=description,
            image=request.FILES['image'] if image else None,
            category =category,
            price =price,)
        return HttpResponse(f"{new_product.name} успешно добавлен")
    return render(request, 'catalog/user_add_product.html', context=context)


# def index(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'catalog/catalog_base.html', context=context)
