from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(view):
    """
    View to return all properties.
    Response is cached in Redis for 15 minutes.
    """
    properties = Property.objects.all().values(
        'property_id', 'title', 'description', 'price', 'location', 'created_at'
    )

    return JsonResponse({
        'count': properties.count(),
        'properties': list(properties)
    }, safe=False)
