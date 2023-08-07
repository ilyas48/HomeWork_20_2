from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **option):
        category_list = [
            {'name': 'Смартфоны и гаджеты', 'description': 'Смартфоны и аксессуары'},
            {'name': 'Умные колонки', 'description': 'Умные колонки Яндекс, JBL, Apple, VK'},
            {'name': 'Телевизоры', 'description': 'Телевизоры для кухни,спальни,гостиной'},
        ]
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)