from django.contrib import admin

from .models import Link, Status


@admin.action(description="Disable selected links")
def disable_links(modeladmin, request, queryset):
    queryset.update(status=Status.INACTIVE)


@admin.action(description="Enable selected links")
def enable_links(modeladmin, request, queryset):
    queryset.update(status=Status.ACTIVE)


class LinkAdmin(admin.ModelAdmin):  # type: ignore
    list_display = ["alias", "url", "hits", "created", "updated", "status"]
    list_filter = ["status"]

    fields = ["id", "created", "updated", "status", "alias", "url", "hits"]
    readonly_fields = ["id", "created", "updated"]

    actions = [disable_links, enable_links]


admin.site.register(Link, LinkAdmin)
