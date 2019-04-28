# Copyright (C) 2019 by Vd.
# This file is part of Rocketgraph, the powerful asynchronous library for telegra.ph.
# Rocketgraph is released under the MIT License (see LICENSE).


from dataclasses import dataclass, asdict
from typing import Optional, List, Union

API_URL = "https://api.telegra.ph/%s"


@dataclass(frozen=True)
class Account:
    """\
    Represents Account object:
    https://telegra.ph/api#Account
    """

    short_name: Optional[str] = None
    author_name: Optional[str] = None
    author_url: Optional[str] = None
    access_token: Optional[str] = None
    auth_url: Optional[str] = None
    page_count: Optional[int] = None

    @classmethod
    def parse(cls, data: dict) -> 'Account':
        return cls(short_name=data.get('short_name'), author_name=data.get('author_name'),
                   author_url=data.get('author_url'), access_token=data.get('access_token'),
                   auth_url=data.get('auth_url'), page_count=data.get('page_count'))


Node = Union[str, 'NodeElement']


@dataclass(frozen=True)
class NodeElement:
    """\
    Represents NodeElement object:
    https://telegra.ph/api#NodeElement
    """

    tag: str
    attrs: Optional[str] = None
    children: Optional[List['Node']] = None

    def render(self):
        return asdict(self)

    @classmethod
    def parse(cls, data):
        if data is None:
            return None
        if isinstance(data, str):
            return data
        if isinstance(data, dict):
            return NodeElement(tag=data['tag'], attrs=data.get('attrs'),
                               children=NodeElement.parse(data.get('children')))
        if isinstance(data, list):
            return [NodeElement.parse(e) for e in data]


@dataclass(frozen=True)
class Page:
    """\
    Represents Page object:
    https://telegra.ph/api#Page
    """

    path: str
    url: str
    title: str
    description: str
    author_name: Optional[str] = None
    author_url: Optional[str] = None
    image_url: Optional[str] = None
    content: Optional[List['Node']] = None
    views: Optional[int] = None
    can_edit: Optional[bool] = None

    @classmethod
    def parse(cls, data: dict) -> 'Page':
        return cls(path=data['path'], url=data['url'], title=data['title'],
                   description=data['description'], author_name=data.get('author_name'),
                   author_url=data.get('author_url'), image_url=data.get('image_url'),
                   content=NodeElement.parse(data.get('content')),
                   views=data.get('views'), can_edit=data.get('can_edit'))


@dataclass(frozen=True)
class PageList:
    """\
    Represents PageViews object:
    https://telegra.ph/api#PageViews
    """

    total_count: int
    pages: Optional[List['Page']] = None

    @classmethod
    def parse(cls, data: dict) -> 'PageList':
        pages = None
        if 'pages' in data:
            pages = [Page.parse(p) for p in data['pages']]
        return cls(total_count=data['total_count'], pages=pages)


@dataclass(frozen=True)
class PageViews:
    """\
    Represents PageViews object:
    https://telegra.ph/api#PageViews
    """

    views: int

    @classmethod
    def parse(cls, data: dict) -> 'PageViews':
        return cls(views=data['views'])
