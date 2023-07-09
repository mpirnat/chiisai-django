from typing import Optional

from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from ninja import errors as ninja_errors
from ninja_apikey.security import APIKeyAuth  # type: ignore

from .alias import UncleanAlias, make_alias
from .models import Link, Status

auth = APIKeyAuth()
router = Router(auth=APIKeyAuth())


class LinkSchema(Schema):
    alias: Optional[str] = None
    url: str


@router.post("/v1/links")
def create_short_url(request, data: LinkSchema):
    alias = data.alias or None
    alias_was_requested = alias is not None
    url = data.url

    try:
        alias = make_alias(url, alias=alias)
    except UncleanAlias as exc:
        raise ninja_errors.ValidationError(str(exc)) from exc

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

    return str(link)


@router.get("/v1/links/{alias}")
def get_short_url_details(request, alias: str):
    link = get_object_or_404(Link, alias=alias, status=Status.ACTIVE)
    return str(link)


# Looking for an API for listing links from the collection,
# or updating an existing link?
# These have been omitted for security reasons.
