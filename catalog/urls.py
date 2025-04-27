from django.urls import path

from catalog.apps import CatalogConfig

from . import views

# определим пространство имен
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
    path('orders/', views.orders, name='orders'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('user_add_product/', views.user_add_product, name='user_add_product')
    # path('contact/', views.contact, name='contact'),

]
