from django.urls import path
from . import views
from catalog.apps import CatalogConfig

# определим пространство имен
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
    path('orders/', views.orders, name='orders'),
    path('contact/', views.contact, name='contact'),

]