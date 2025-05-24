from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm, ProductModeratorForm
from .models import Category, Product


class ProductListView(ListView):
    """ Класс представления для списка продуктов на главной странице  """
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"
    paginate_by = 3


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Класс представления формы для создания продукта"""
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


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
