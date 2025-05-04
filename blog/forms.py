from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """ Метод для передачи полей модели статьи в обработчик в views.py. Нужен для полей с загружаемыми файлами."""
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'published',]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
