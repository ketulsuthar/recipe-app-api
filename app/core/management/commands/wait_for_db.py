import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available
    """
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_con = None
        while not db_con:
            try:
                db_con = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting for 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
