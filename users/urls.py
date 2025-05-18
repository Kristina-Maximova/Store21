from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from .views import RegisterView


# определим пространство имен
app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),

]
