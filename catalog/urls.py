from django.urls import path

from catalog.apps import CatalogConfig

from . import views

# определим пространство имен
app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.ProductListView.as_view(), name='home'),
    path('product/new/', views.ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product' ),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/', views.category, name='category'),
    path('orders/', views.orders, name='orders'),
    # path('product/detail/<int:product_id>/', views.product_detail, name='product_detail'),

    # path('contact/', views.contact, name='contact'),
]
