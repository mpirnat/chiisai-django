from django.conf import settings
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Link, Status


def home(request):
    return JsonResponse({"hello": "world"})


def redirect_alias_to_url(request, alias: str):
    """
    Look up and redirect to a long URL.
    """
    link_queryset = Link.objects.filter(alias=alias, status=Status.ACTIVE)

    if settings.SHOULD_COUNT_HITS:
        link_queryset = link_queryset.select_for_update()
        with transaction.atomic():
            link = get_object_or_404(link_queryset)
            link.hits += 1
            link.save()
    else:
        link = get_object_or_404(link_queryset)

    return HttpResponseRedirect(link.url)
