# Copyright (C) 2019 by Vd.
# This file is part of Rocketgraph, the powerful asynchronous library for telegra.ph.
# Rocketgraph is released under the MIT License (see LICENSE).


import logging

from ..version import version

logger = logging.getLogger('rocketgraph.connectors.connector')

USER_AGENT = f'Rocketgraph/{version()}'


class Connector:
    async def init(self):
        raise NotImplementedError

    async def shutdown(self):
        raise NotImplementedError

    async def request(self, method: str, data: dict) -> dict:
        raise NotImplementedError
