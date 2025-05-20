from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class StoreUser(AbstractUser):
    username = models.CharField(max_length=25, blank=True, null=True,
                                verbose_name='Имя пользователя',
                                help_text='Введите Ваше имя')
    email = models.EmailField(unique=True, verbose_name='Email',
                              help_text='Введите эл.почту')
    phone_number = PhoneNumberField(region="RU",
                                    blank=True, null=True,
                                    verbose_name='Телефон', )
    avatar = models.ImageField(upload_to='users/avatars/',
                               blank=True, null=True,
                               verbose_name='Аватар',
                               help_text='Загрузите фото, по-желанию')
    country = models.CharField(max_length=25, verbose_name='Страна',
                               help_text='Ваша страна',
                               blank=True, null=True)

    groups = models.ManyToManyField(Group, blank=True, related_name="user_set")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="user_permissions_set")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
