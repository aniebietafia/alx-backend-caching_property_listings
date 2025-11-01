from django.core.management.base import BaseCommand
from properties.utils import get_redis_cache_metrics


class Command(BaseCommand):
    help = 'Display Redis cache metrics'

    def handle(self, *args, **options):
        metrics = get_redis_cache_metrics()
        self.stdout.write(self.style.SUCCESS('Cache metrics retrieved successfully!'))
