from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand # noqa


class Command(BaseCommand):
    """ Django command to wait for db"""
    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 secound...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
