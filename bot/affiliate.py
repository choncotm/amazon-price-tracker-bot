import os
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


def with_affiliate_tag(url: str) -> str:
    tag = os.environ.get("AMAZON_ASSOCIATE_TAG")
    if not tag:
        return url

    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query))
    query["tag"] = tag
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))
