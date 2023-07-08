from typing import Optional

from ninja import Router, Schema

from .models import Link

router = Router()


class LinkSchema(Schema):
    alias: Optional[str] = None
    url: str


@router.post("/v1/links")
def create_short_url(request, data: LinkSchema):
    link = Link(alias=data.alias, url=data.url)
    link.save()
    return str(link)


@router.get("/v1/links/{alias}")
def get_short_url_details(request, alias: str):
    link = Link.objects.get(alias=alias)
    return str(link)


# Looking for an API for listing links from the collection,
# or updating an existing link?
# These have been omitted for security reasons.
