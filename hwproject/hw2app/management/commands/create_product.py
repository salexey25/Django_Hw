from django.core.management.base import BaseCommand
from hw2app.models import ProductModel, OrderModel

class Command(BaseCommand):
    help = 'Add new product'
    def handle(self, *args, **kwargs):
        product = ProductModel(name='fridge',
                               description='LG 456-gf',
                               price=9543.56,
                               count=1,
                               )
        product.save()
        self.stdout.write(f'{product}')
