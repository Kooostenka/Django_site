from django.core.management.base import BaseCommand
import csv
from women.models import Women


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = Women.objects.filter(is_published=True)

        with open("new_file.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            for user in users:
                writer.writerow([user.title, user.cat])
