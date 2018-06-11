# Author: Junior Tada
from sanic import Sanic
import redis

# Define app Sanic
app = Sanic()
__version__ = '0.1'
__author__ = 'Junior Tada'

# Principal
from app.controller import main

# Blueprints
from app.webservice.controller import webservice

# Registra blueprints
app.blueprint(webservice, url_prefix='/webservice')