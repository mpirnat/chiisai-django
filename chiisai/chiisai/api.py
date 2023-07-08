from ninja import NinjaAPI

from shortener.api import router as shortener_router

api = NinjaAPI()

api.add_router("/shortener/", shortener_router)
