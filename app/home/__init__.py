from flask import Blueprint

home = Blueprint('home', __name__, template_folder='home_templates')

from . import routes