from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ["alias", "url", "hits", "created", "updated", "status"]
    fields = ["id", "created", "updated", "status", "alias", "url", "hits"]
    readonly_fields = ["id", "created", "updated"]


admin.site.register(Link, LinkAdmin)
