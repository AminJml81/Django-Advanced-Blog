from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from faker import Faker
import random

from accounts.models import User, Profile
from ...models import Post, Category


class Command(BaseCommand):
    help = "Inserts Sample posts."

    def add_arguments(self, parser):
        parser.add_argument("--number", nargs='?', type=int, default=1, help='number of posts to create.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()
        self.categories = [
            'IT',
            'Programming',
            'IOT',
            'Software',
            'Hardware',
            'Data Science',
            'Machine Learning'
        ]

    def handle(self, *args, **options):
        user = User.objects.create_user(
            email = self.fake.email(),
            password = self.fake.password() 
        )
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=4)
        profile.save()
        
        categories_objects = []
        for cat in self.categories:
            cat, created = Category.objects.get_or_create(name=cat)
            categories_objects.append(cat)

        for _ in range(options['number']):
            Post.objects.create(
                category = random.choice(categories_objects),
                title = self.fake.text(max_nb_chars=10),
                content = self.fake.paragraph(nb_sentences=5),
                author = profile,
                published_date = timezone.now(),        
            )