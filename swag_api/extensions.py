"""
.. module: swag_api.extensions
    :copyright: (c) 2017 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
"""
from raven.contrib.flask import Sentry
from swag_client.backend import SWAGManager


sentry = Sentry()

swag = SWAGManager()

