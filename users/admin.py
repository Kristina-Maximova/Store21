from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import StoreUser

admin.site.register(StoreUser, UserAdmin)