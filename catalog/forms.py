from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Наименование продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
                                                        'placeholder': 'Описание продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Введите цену продукта в рублях'})
