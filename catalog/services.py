from django.core.cache import cache
from .models import Product
from config.settings import CACHE_ENABLED


class ProductService:
    """ Класс для получения выборки по продуктам """

    @staticmethod
    def get_products_by_category(category_id):
        """ Выборка продуктов по категории"""
        products = Product.objects.filter(category_id=category_id)
        if not products.exists():
            return None
        return products

    @staticmethod
    def get_cached_products():
        """ метод получения продуктов из кэша"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = "products_list"
        products = cache.get_or_set(key, lambda: Product.objects.all())
        return products
