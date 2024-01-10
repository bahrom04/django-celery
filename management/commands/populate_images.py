from django.core.management.base import BaseCommand
from test_app.models import RandomImage

# https://github.com/bbelderbos/django-n-plus-one-demo/blob/main/books/management/commands/populate_data.py
class Command(BaseCommand):
    help = 'Populates the database with random image.'

    def handle(self, *args, **options):
        images = []
        for i in range(100):
            random_image = RandomImage(image=f'{i}.jpg')
            images.append(random_image)

        RandomImage.objects.bulk_create(images)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(images)} images'))