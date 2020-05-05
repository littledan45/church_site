from django.core.management import BaseCommand

from churches.management.commands._churches import create_churches
from sermons.management.commands._sermons import create_sermons
from speakers.management.commands._speakers import create_speakers
from schedules.management.commands._events import create_events


class Command(BaseCommand):
    help = 'Adds sample data'

    def handle(self, *args, **options):
        create_churches()
        self.stdout.write(self.style.SUCCESS('Successfully created churches'))
        create_speakers()
        self.stdout.write(self.style.SUCCESS('Successfully created speakers'))
        create_events()
        self.stdout.write(self.style.SUCCESS('Successfully created events'))
        create_sermons()
        self.stdout.write(self.style.SUCCESS('Successfully created sermons'))
