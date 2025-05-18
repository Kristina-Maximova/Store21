from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StoreUser


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():   # в self.fields() получим словарь: {название поля:значение}
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-class" # поменять на 'form-control'


class StoreUserCreationForm(UserCreationForm):
    """ Форма для регистрации пользователя"""
    username = forms.CharField(max_length=100,
                               required=True)  # если не указать как обязательное, будет ошибка при добавлении нового,
    usable_password = None

    class Meta(UserCreationForm.Meta):
        model = StoreUser
        fields = ('email', 'username', 'password1', 'password2',)

