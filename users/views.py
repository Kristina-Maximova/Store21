import os

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from dotenv import load_dotenv

from .forms import StoreUserCreationForm

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

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)
