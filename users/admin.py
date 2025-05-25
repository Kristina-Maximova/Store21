from django.contrib import admin

from .models import StoreUser

# Register your models here.


@admin.register(StoreUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    search_fields = ('email',)
