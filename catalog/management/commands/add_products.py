from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        # Создаем новые записи
        category, _ = Category.objects.get_or_create(name='Ручной инструмент',
                                                     description='Простые и надежные инструменты для дома')
        products = [
            {"name": "молоток",
             "category": category,
             "price": 1000.0,},
            {"name": "отвертка",
             "category": category,
             "price": 150.0
             },
        ]
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))



        # # Вместо создания новых можно загружать из фикстур
        # call_command('loaddata', 'categories_fixture.json')
        # call_command('loaddata', 'products_fixture.json')




