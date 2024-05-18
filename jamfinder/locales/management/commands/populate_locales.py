from django.core.management.base import BaseCommand
from locales.models import Local

class Command(BaseCommand):
    help = 'Populate the database with dummy data for locales'

    def handle(self, *args, **kwargs):
        for i in range(1, 21):
            Local.objects.create(
                name=f'Rehearsal Room {i}',
                type_of_studio='Recording Studio',
                address=f'Fake Street {i}, Madrid',
                opening_hours='10:00 - 22:00',
                price=20.0,
                services='Service A, Service B',
                phone_number=f'12345678{i}'
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
