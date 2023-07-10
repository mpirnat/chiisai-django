from datetime import datetime
from typing import Optional

from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from ninja import Field, Router, Schema
from ninja import errors as ninja_errors
from ninja_apikey.security import APIKeyAuth  # type: ignore
from pydantic import HttpUrl

from .alias import UncleanAlias, make_alias
from .models import Link, Status

auth = APIKeyAuth()
router = Router(auth=APIKeyAuth())


class LinkInputSchema(Schema):
    alias: Optional[str] = Field(default=None, max_length=200)
    url: HttpUrl


class LinkOutputSchema(Schema):
    alias: str
    url: HttpUrl
    hits: int
    created: datetime
    updated: datetime


@router.post("/v1/links", response=LinkOutputSchema)
def create_short_url(request, data: LinkInputSchema):
    alias = data.alias or None
    alias_was_requested = alias is not None
    url = data.url

    try:
        alias = make_alias(url, alias=alias)
    except UncleanAlias as exc:
        raise ninja_errors.ValidationError(
            [
                {
                    "loc": ["body", "data", "alias"],
                    "msg": str(exc),
                    "type": "value_error.value_error",
                }
            ]
        ) from exc

    link = Link(alias=data.alias, url=data.url)
    try:
        link.save()
    except IntegrityError as exc:
        # That alias is already claimed; you can't have it
        if alias_was_requested:
            link = Link.objects.get(alias=alias)
            if url != link.url:
                raise ninja_errors.HttpError(403, "Forbidden") from exc

        # Hashed to the same thing? Be idempotent
        else:
            pass

    return link


@router.get("/v1/links/{alias}", response=LinkOutputSchema)
def get_short_url_details(request, alias: str):
    link = get_object_or_404(Link, alias=alias, status=Status.ACTIVE)
    return link


# Looking for an API for listing links from the collection,
# or updating an existing link?
# These have been omitted for security reasons.
