from django.db import models, transaction


class Status(models.TextChoices):
    ACTIVE = "A", "Active"
    INACTIVE = "I", "Inactive"


class Link(models.Model):
    id = models.BigAutoField(primary_key=True)

    alias = models.SlugField(max_length=200, unique=True)
    url = models.URLField(max_length=2048)
    hits = models.PositiveBigIntegerField(default=0)

    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.ACTIVE
    )
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

    def get_queryset(self):
        return self.__class__.objects.filter(id=self.id)

    @transaction.atomic()
    def increment_hits(self, amount: int = 1):
        obj = self.get_queryset().select_for_update().get()
        obj.hits += amount
        obj.save()
        return obj
