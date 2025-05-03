from django.db import models


# Create your models here.
class Post(models.Model):
    """ Класс для создания записи в блоге """
    title = models.CharField(max_length=100,
                             verbose_name="Заголовок",
                             help_text="Заголовок", )
    content = models.TextField(verbose_name="Текстовый контент",
                               help_text="Текст поста",
                               null=True,
                               blank=True, )
    image = models.ImageField(
        upload_to="photos/blog",
        verbose_name="Изображение",
        default='photos/blog/default_post.jpg',
        help_text='Загрузите изображение',
        blank=True,
        null=True, )
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True,
                                  verbose_name="Дата обновления", )
    published = models.BooleanField(default=False, )
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "published", "created_at", "updated_at", 'views_count']
