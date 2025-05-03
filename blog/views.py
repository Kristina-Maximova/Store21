from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView,
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import PostForm
from .models import Post


# Create your views here.
class PostListView(ListView):
    """ Метод отображения списка статей"""
    model = Post
    template_name = "blog/post_list.html"
    # <app_name>/<model_mame>_<action>  надо называть шаблоны так, тогда можно не указывать template_name=""
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published=True)


class PostDetailView(DetailView):
    """ Метод отображения одной статьи """
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    """ Метод для создания новой статьи """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    """ Метод для редактирования статьи """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    # success_url = reverse_lazy("blog:post_list")
    # если возвращать на страницу post_detail, то success_url надо получать из метода
    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    """ Метод для удаления статьи """
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
