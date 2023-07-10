from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Link, Status


def home(request):
    return JsonResponse({"hello": "world"})


def redirect_alias_to_url(request, alias: str):
    """
    Look up and redirect to a long URL.
    """
    link = get_object_or_404(Link, alias=alias, status=Status.ACTIVE)
    if settings.SHOULD_COUNT_HITS:
        link.increment_hits()
    return HttpResponseRedirect(link.url)
