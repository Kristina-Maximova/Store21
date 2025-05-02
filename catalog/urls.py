from django.urls import path

from catalog.apps import CatalogConfig
from . import views


# определим пространство имен
app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('product/new/', views.ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product' ),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    # path('category/<str:category_name>/', views.CategoryListView.as_view(), name='category'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/', views.CatalogListView.as_view(), name='catalog'),
    path('orders/', views.OrdersTemplateView.as_view(), name='orders' ),

]
