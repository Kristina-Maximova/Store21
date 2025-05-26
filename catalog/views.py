from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from django.conf import settings
from unicodedata import category

from .forms import ProductForm, ProductModeratorForm
from .models import Category, Product
from .services import ProductService


class ProductListView(ListView):
    """ Класс представления для списка продуктов на главной странице  """
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        return ProductService.get_cached_products()


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Класс представления формы для создания продукта"""
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # назначение текущего пользователя владельцем
        form.instance.owner = self.request.user
        # сохранение изменений происходит в родительском методе
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # или логирование ошибок
        return super().form_invalid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Класс представления формы для редактирования полей продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        user = self.request.user
        # if user.has_perm('catalog.can_unpublish_product') and not user.has_perm('catalog.can_view_permission') :
        #     return ProductModeratorForm
        if user.groups.filter(name='moderators').exists():
            return ProductModeratorForm
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """ Класс представления формы для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not (self.request.user == obj.owner or self.request.user.groups.filter(name='moderators').exists()):
            raise PermissionDenied("У вас нет прав удалять этот продукт.")
        return obj


if settings.CACHE_ENABLED:
    cache_decorator = method_decorator(cache_page(60 * 2), name='dispatch')
else:
    def cache_decorator(cls):
        return cls

@cache_decorator
class ProductDetailView(LoginRequiredMixin, DetailView):
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
        # queryset = super().get_queryset()
        # return queryset.filter(category__name='Ручной инструмент')
        category_id = self.kwargs.get('category_id')  # Получаем category_id из URL
        products = ProductService.get_products_by_category(category_id)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем category_name в контекст
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        context['category_name'] = category.name
        return context


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
