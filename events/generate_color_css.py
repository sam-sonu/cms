from .models import UpcomingEventsModel
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Generate colors css for first time'

    def handle(self, *args, **options):
        """ Do your work here """
        t = UpcomingEventsModel.objects.get()
        if t:
            t.save()
