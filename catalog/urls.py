from django.urls import path
from . import views


# определим пространство имен
app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]