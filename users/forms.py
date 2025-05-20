from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField

from .models import StoreUser


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # в self.fields() получим словарь: {название поля:значение}
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class StoreUserCreationForm(StyleFormMixin, UserCreationForm):
    """ Форма для регистрации пользователя"""

    class Meta(UserCreationForm.Meta):
        model = StoreUser
        fields = ('email', 'password1', 'password2',)


class StoreUserChangeForm(StyleFormMixin, forms.ModelForm):
    """ Форма для редактирования профиля пользователя"""
    # usable_password = None

    class Meta(UserCreationForm.Meta):
        model = StoreUser
        fields = ('email', 'phone_number', 'avatar', 'country',)
        # exclude = ('',)
