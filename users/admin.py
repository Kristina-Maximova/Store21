from django.contrib import admin

from .models import StoreUser

# Register your models here.


@admin.register(StoreUser)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)
