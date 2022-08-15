from catalog.models import Author, Quote
from django.core.management.base import BaseCommand
import random
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create faker values to DB. Warning: use 1 time!'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, choices=range(1, 10000), help='Number of the creating values')

    def handle(self, *args, **options):
        number = options['number']
        authors = []
        quotes = []
        for i in range(number):
            author = Author(name=fake.name(),
                            description=fake.text())
            authors.append(author)
        Author.objects.bulk_create(authors)
        for i in range(number):
            quote = Quote(message=fake.text(),
                          author_id=Author.objects.get(pk=i+1).pk)
            quotes.append(quote)
        Quote.objects.bulk_create(quotes)
        self.stdout.write(self.style.SUCCESS('DB is populated %s values successfully!' % number))
