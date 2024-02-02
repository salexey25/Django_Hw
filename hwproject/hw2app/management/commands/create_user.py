from django.core.management.base import BaseCommand
from hw2app.models import ClientModel

class Command(BaseCommand):
    help = 'Add new client'
    def handle(self, *args, **kwargs):
        user = ClientModel(name='Alex',
                           email='alex@example.com',
                           phone=89994445566,
                           address='SPb Nevskiy')
        user.save()
        self.stdout.write(f'{user}')

