from flask import Blueprint
from libs.external_api import ExternalApi

bp = Blueprint('hello', __name__, url_prefix='/hello')
api = ExternalApi(bp)

from .hello import HelloGetApi
