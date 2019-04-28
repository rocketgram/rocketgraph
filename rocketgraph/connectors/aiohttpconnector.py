# Copyright (C) 2019 by Vd.
# This file is part of Rocketgraph, the powerful asynchronous library for telegra.ph.
# Rocketgraph is released under the MIT License (see LICENSE).


import asyncio
import json
import logging

import aiohttp

from .connector import Connector, USER_AGENT
from .. import types

json_encoder = json.dumps
json_decoder = json.loads

try:
    import ujson

    json_encoder = ujson.dumps
    json_decoder = ujson.loads
except ModuleNotFoundError:
    pass

logger = logging.getLogger('rocketgraph.connectors.aiohttpconnector')

HEADERS = {'Content-Type': 'application/json', 'User-Agent': USER_AGENT}


class AioHttpConnector(Connector):
    __slots__ = ('__api_url', '__session', '__timeout')

    def __init__(self, *, timeout: int = 35, api_url: str = types.API_URL):
        self.__api_url = api_url
        self.__session = aiohttp.ClientSession(loop=asyncio.get_event_loop())
        self.__timeout = timeout

    async def init(self):
        pass

    async def shutdown(self):
        await self.__session.close()

    async def request(self, method: str, data: dict) -> dict:
        try:
            url = self.__api_url % method

            response = await self.__session.post(url, data=json_encoder(data), headers=HEADERS,
                                                 timeout=self.__timeout)

            return json_decoder(await response.read())
        except json.decoder.JSONDecodeError as e:
            raise
        except asyncio.CancelledError:
            raise
        except Exception as e:
            raise
