from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER

from .forms import StoreUserChangeForm, StoreUserCreationForm
from .models import StoreUser


class RegisterView(CreateView):
    """ Представление для регистрации нового пользователя """
    template_name = 'users/register.html'
    form_class = StoreUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def send_welcome_email(self, user_email):
        subject = 'Store'
        message = 'Вы успешно зарегистрировались. Добро пожаловать в наш интернет-магазин "Store"!'
        from_email = EMAIL_HOST_USER  # EMAIL_HOST_USER из settings
        recipient_list = [user_email, ]
        send_mail(subject, message, from_email, recipient_list)

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Представление для редактирования профиля пользователя """
    model = StoreUser
    form_class = StoreUserChangeForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('catalog:home')

    def get_objects(self, queryset=None):
        return self.request.user
