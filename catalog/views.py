from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import ProductForm

from .models import Product, Category


class ProductListView(ListView):
    """ Класс представления для списка продуктов на главной странице  """
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 3


class ProductCreateView(CreateView):
    """ Класс представления формы для создания продукта"""
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    """ Класс представления формы для редактирования полей продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    """ Класс представления формы для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
    """ Класс представления для информации о продукте"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CategoryListView(ListView):
    """ Класс представления для списка продуктов определенной категории """
    model = Product
    template_name = "catalog/category_1.html"
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(category__name='Ручной инструмент')

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category_name = self.kwargs['category_name']
    #     return queryset.filter(category__name=category_name)


class ContactsTemplateView(TemplateView):
    """ Класс представления для страницы контактов """
    template_name = "catalog/contacts.html"


class CatalogListView(ListView):
    """ Класс представления для списка категорий"""
    model = Category
    template_name = 'catalog/catalog.html'
    context_object_name = 'categories'


class OrdersTemplateView(TemplateView):
    template_name = "catalog/orders.html"


# def contacts(request):
#     if request.method == 'POST':  # POST - словарь с параметрами
#         # Получение данных из формы
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     return render(request, 'catalog/contacts.html')


# def product_detail(request, product_id):
#     # product = Product.objects.get(id=product_id)
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/product_detail.html', context=context)


# def product_form(request):
#     categories = Category.objects.all()
#     context = {
#         'categories': categories,
#     }
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         image = request.FILES.get("image") # так сюда передается файл
#         price = request.POST.get("price")
#         category_id = request.POST.get('category')
#         category = Category.objects.get(id=category_id)
#         new_product = Product.objects.create(
#             name=name,
#             description=description,
#             image=request.FILES['image'] if image else None,
#             category =category,
#             price =price,)
#         return HttpResponse(f"{new_product.name} успешно добавлен")
#     return render(request, 'catalog/user_add_product.html', context=context)


# def home(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'catalog/home.html', context=context)


# def home(request):
#     products = Product.objects.all()
#     paginator = Paginator(products, 3)  # 3 элемента на странице
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'catalog/home.html', {'page_obj': page_obj})
