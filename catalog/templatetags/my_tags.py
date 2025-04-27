from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """ Шаблонный фильтр, добавляет media/ к пути до изображений"""
    if path:
        return f"media/{path}"
    return "#"
