from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import StoreUserCreationForm
from django.core.mail import send_mail
import os
from dotenv import load_dotenv

load_dotenv(override=True)


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = StoreUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def send_welcome_email(self, user_email):
        subject = 'Store'
        message = 'Вы успешно зарегистрировались. Добро пожаловать в наш интернет-магазин "Store"!'
        from_email = os.getenv('EMAIL_HOST_USER')  # EMAIL_HOST_USER из settings
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)
