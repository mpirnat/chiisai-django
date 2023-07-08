from django.http import HttpResponseRedirect, JsonResponse

from .models import Link


def home(request):
    return JsonResponse({"hello": "world"})


def redirect_alias_to_url(request, alias: str):
    link = Link.objects.get(alias=alias)
    # TODO: increment link.hits
    return HttpResponseRedirect(link.url)
