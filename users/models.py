from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField


class StoreUser(AbstractUser):
    username = models.CharField(max_length=25, blank=True, null=True, verbose_name='Имя пользователя',
                                help_text='Введите Ваше имя')
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите эл.почту')
    phone_number = PhoneNumberField(region="RU", blank=True, null=True, verbose_name='Телефон', )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите фото, по-желанию')
    country = models.CharField(max_length=25, verbose_name='Страна', help_text='Ваша страна', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    groups = models.ManyToManyField(
        Group,
        related_name='storeuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='storeuser',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='storeuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='storeuser',
    )
