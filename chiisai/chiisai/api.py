from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI

from shortener.api import router as shortener_router

api = NinjaAPI(docs_decorator=staff_member_required)

api.add_router("/shortener/", shortener_router)
