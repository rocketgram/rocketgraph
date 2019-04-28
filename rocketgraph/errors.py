# Copyright (C) 2019 by Vd.
# This file is part of Rocketgraph, the powerful asynchronous library for telegra.ph.
# Rocketgraph is released under the MIT License (see LICENSE).


class RocketgraphError(Exception):
    """Base exception for all RocketgraphErrors"""
    pass


class RocketgraphNetworkError(RocketgraphError):
    """\
    Exception indicates error from connector.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def __str__(self):
        return "Network error: %s: %s" % (type(self.exception).__name__, self.exception)


class RocketgraphParseError(RocketgraphError):
    """\
    Exception indicates error from json-parser.
    """

    def __init__(self, exception: Exception):
        self.exception = exception

    def __str__(self):
        return "Parser error: %s: %s" % (type(self.exception).__name__, self.exception)


class RocketgraphRequestError(RocketgraphError):
    """\
    Exception for all request-related errors.
    """

    def __init__(self, error: str):
        self.error = error

    def __str__(self):
        return self.error
