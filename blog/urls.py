from django.urls import path
from blog.apps import BlogConfig

from . import views

# определим пространство имен
app_name = BlogConfig.name

urlpatterns = []
