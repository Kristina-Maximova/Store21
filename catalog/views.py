from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Category, Product


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
