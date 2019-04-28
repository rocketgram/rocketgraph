# Copyright (C) 2019 by Vd.
# This file is part of Rocketgraph, the powerful asynchronous library for telegra.ph.
# Rocketgraph is released under the MIT License (see LICENSE).


import logging
from typing import Optional, List
from typing import TYPE_CHECKING

from .errors import RocketgraphRequestError
from .types import Account, Node, NodeElement, Page, PageList, PageViews

if TYPE_CHECKING:
    from .connectors import Connector

logger = logging.getLogger('rocketgraph.client')


class Client:
    __slots__ = ('__token', '__connector', '__own_connector')

    def __init__(self, token: Optional[str], *, connector: Optional['Connector'] = None):
        """\

        :param token: telegraph's token
        :param session: aiohttp.ClientSession
        """

        self.__token = token

        self.__connector = connector
        self.__own_connector = False
        if not self.__connector:
            from .connectors import AioHttpConnector
            self.__connector = AioHttpConnector()
            self.__own_connector = True

    @property
    def token(self) -> str:
        """Bot's token."""

        return self.__token

    async def init(self):
        """\
        Initializes connector if it explicitly specified.
        """

        if self.__own_connector:
            await self.__connector.init()

    async def shutdown(self):
        """\
        Closes connector it explicitly specified.
        """
        if self.__own_connector:
            await self.__connector.shutdown()

    async def create_account(self, short_name: str, author_name: Optional[str] = None,
                             author_url: Optional[str] = None) -> 'Account':
        """\
        Implements createAccount call:
        https://telegra.ph/api#createAccount

        Creates new account and overrides Client's token.

        :param short_name:
        :param author_name:
        :param author_url:
        """

        data = dict(
            short_name=short_name,
            author_name=author_name,
            author_url=author_url,
        )

        response = await self.__connector.request('createAccount', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        account = Account.parse(response['result'])
        self.__token = account.access_token

        return account

    async def create_page(self, title: str, content: List['Node'], author_name: Optional[str] = None,
                          author_url: Optional[str] = None, return_content: Optional[bool] = None) -> 'Page':
        """\
        Implements createPage call:
        https://telegra.ph/api#createPage

        Creates new account and overrides Client's token.

        :param title:
        :param content:
        :param author_name:
        :param author_url:
        :param return_content:
        """

        data = dict(
            title=title,
            content=[c.render() if isinstance(c, NodeElement) else c for c in content],
            author_name=author_name,
            author_url=author_url,
            return_content=return_content,
        )

        response = await self.__connector.request('createPage', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return Page.parse(response['result'])

    async def edit_account_info(self, short_name: str, author_name: Optional[str] = None,
                                author_url: Optional[str] = None) -> 'Account':
        """\
        Implements editAccountInfo call:
        https://telegra.ph/api#editAccountInfo

        :param short_name:
        :param author_name:
        :param author_url:
        """

        data = dict(
            access_token=self.token,
            short_name=short_name,
            author_name=author_name,
            author_url=author_url
        )

        response = await self.__connector.request('editAccountInfo', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return Account.parse(response['result'])

    async def edit_page(self, path: str, title: str, content: List['Node'], author_name: Optional[str] = None,
                        author_url: Optional[str] = None, return_content: Optional[bool] = None):
        """\
        Implements editPage call:
        https://telegra.ph/api#editPage

        :param path:
        :param title:
        :param content:
        :param author_name:
        :param author_url:
        :param return_content:
        """

        data = dict(
            access_token=self.token,
            path=path,
            title=title,
            content=[c.render() if isinstance(c, NodeElement) else c for c in content],
            author_name=author_name,
            author_url=author_url,
            return_content=return_content,
        )

        response = await self.__connector.request('editPage', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return Page.parse(response['result'])

    async def get_account_info(self, fields: Optional[List[str]]) -> 'Account':
        """\
        Implements getAccountInfo call:
        https://telegra.ph/api#getAccountInfo

        :param fields:
        """

        if not fields:
            fields = ['short_name', 'author_name', 'author_url']

        data = dict(
            access_token=self.token,
            path=fields,
        )

        response = await self.__connector.request('getAccountInfo', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return Account.parse(response['result'])

    async def get_page(self, path: str, return_content: Optional[bool] = None) -> 'Page':
        """\
        Implements getPage call:
        https://telegra.ph/api#getPage

        :param path:
        :param return_content:
        """

        data = dict(
            access_token=self.token,
            path=path,
            return_content=return_content,
        )

        response = await self.__connector.request('getPage', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return Page.parse(response['result'])

    async def get_page_list(self, offset: Optional[int] = None, limit: Optional[int] = None) -> 'PageList':
        """\
        Implements getPageList call:
        https://telegra.ph/api#getPageList

        :param offset:
        :param limit:
        """

        data = dict(
            access_token=self.token,
            offset=offset,
            limit=limit,
        )

        response = await self.__connector.request('getPageList', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return PageList.parse(response['result'])

    async def get_views(self, path: str, year: Optional[int] = None, month: Optional[int] = None,
                        day: Optional[int] = None, hour: Optional[int] = None) -> 'PageViews':
        """\
        Implements getViews call:
        https://telegra.ph/api#getViews

        :param path:
        :param year:
        :param month:
        :param day:
        :param hour:
        """

        data = dict(
            access_token=self.token,
            path=path,
            year=year,
            month=month,
            day=day,
            hour=hour
        )

        response = await self.__connector.request('getViews', data)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        return PageViews.parse(response['result'])

    async def revoke_access_token(self) -> 'Account':
        """\
        Implements revokeAccessToken call:
        https://telegra.ph/api#revokeAccessToken

        Overrides Client's token.
        """

        data = dict(
            access_token=self.token
        )

        response = await self.__connector.request('revokeAccessToken', data)
        print(response)

        if not response['ok']:
            raise RocketgraphRequestError(response.get('error'))

        account = Account.parse(response['result'])
        self.__token = account.access_token
        return account
