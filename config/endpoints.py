""" Configure your endpoints here.
    The endpoints are a dictionary of routes and handlers which the app will
    use to construct the routes.
"""
from src.handlers import *
from schemas import *

# endpoints = [
#     {"route": "", "handler": DefaultHandler}
# ]

""" This is an example config/testing
"""
endpoints = [
    {"route": r"/?$", "handler": HelloHandler, "name": "hello"}
]