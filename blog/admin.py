from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published', 'created_at', 'views_count']
    list_filter = ('views_count','title','created_at')
    search_fields = ('title',)