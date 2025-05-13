from django import forms
from django.core.exceptions import ValidationError

from .models import Product
from config.settings import SPAM_LIST
import re


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # в self.fields() получим словарь: {название поля:значение}
            field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    """ Форма модели продукта для передачи в представления"""

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in SPAM_LIST:
            if name and re.search(rf'\b{word}\b', name, re.IGNORECASE):
                self.add_error('name', f'В названии продукта не должно быть слова: {word}')

            if description and re.search(rf'\b{word}\b', description, re.IGNORECASE):
                self.add_error('description', f'В описании продукта не должно быть слова: {word}')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and float(price) < 0.0:
            raise ValidationError('Цена продукта не может быть отрицательной.')
        return price
