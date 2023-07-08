from django.db import models


class Link(models.Model):
    id = models.BigAutoField(primary_key=True)

    alias = models.SlugField(max_length=200, unique=True)
    url = models.URLField(max_length=2048)
    hits = models.PositiveBigIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "created"
        ordering = ["-created", "alias"]
        indexes = [
            models.Index(fields=["created"]),
            models.Index(fields=["updated"]),
            models.Index(fields=["url"]),
            models.Index(fields=["hits"]),
        ]
