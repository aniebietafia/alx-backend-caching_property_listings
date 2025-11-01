from django.core.cache import cache
from .models import Property


def get_all_properties():
    """
    Fetch all properties from cache or database.
    Caches the queryset in Redis for 1 hour (3600 seconds).

    Returns:
        QuerySet: All Property objects
    """
    # Try to get cached data
    cached_properties = cache.get('all_properties')

    if cached_properties is not None:
        print("Returning cached properties")  # Debug log
        return cached_properties

    # If not in cache, fetch from database
    print("Fetching properties from database")  # Debug log
    properties = Property.objects.all()

    # Convert to list to make it serializable for Redis
    properties_list = list(properties.values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    ))

    # Store in cache for 1 hour (3600 seconds)
    cache.set('all_properties', properties_list, 3600)

    return properties_list
